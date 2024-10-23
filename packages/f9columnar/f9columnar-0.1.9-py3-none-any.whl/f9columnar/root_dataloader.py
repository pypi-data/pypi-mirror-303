import copy
import datetime
import glob
import logging
import multiprocessing
import os
import re
from concurrent.futures import ProcessPoolExecutor

import awkward as ak
import numpy as np
import torch
import uproot
from torch.utils.data import DataLoader, IterableDataset
from tqdm import tqdm
from uproot.exceptions import KeyInFileError

from f9columnar.dataloader_monitor import WorkerHeartbeat, WorkerLogger
from f9columnar.utils.helpers import get_file_size, get_ms_time, get_num_entries


class ROOTEventIterator:
    def __init__(
        self,
        root_file,
        name,
        step_size="100 MB",
        postifx="NOMINAL",
        entry_start=None,
        entry_stop=None,
        filter_name=None,
        filter_branch=None,
        desc_dct=None,
    ):
        """Class for abstracting batch ROOT file iteration with uproot iterate method.

        Parameters
        ----------
        root_file : str
            ROOT file path.
        name : str
            Arbitrary name for this iterator.
        step_size : str, optional
            Size of batch events, by default "100 MB".
        postifx : str, optional
            ROOT file entries, by default "NOMINAL".
        entry_start : int, optional
            Event number to start iteration at, by default None.
        entry_stop : int, optional
            Event number at which to stop iteration at, by default None.
        filter_name : str, optional
            See [2], by default None.
        filter_branch : _type_, optional
            See [2], by default None.
        desc_dct : dict, optional
            Description dictionary for additional information, by default None.

        References
        ----------
        [1] - https://uproot.readthedocs.io/en/latest/basic.html#iterating-over-intervals-of-entries
        [2] - https://uproot.readthedocs.io/en/latest/uproot.behaviors.TBranch.HasBranches.html#uproot-behaviors-tbranch-hasbranches-iterate
        [3] - https://awkward-array.org/doc/main/

        """
        self.root_file, self.name = root_file, name

        assert "mb" in step_size.lower() in step_size.lower(), "Step size must be in MB!"
        self.step_size = step_size
        self.float_step_size = float(re.search(r"\d+(\.\d+)?", step_size).group())

        self.postfix = postifx
        self.entry_start, self.entry_stop = entry_start, entry_stop

        self.filter_name, self.filter_branch = filter_name, filter_branch

        if desc_dct is None:
            self.desc_dct = {}
        else:
            self.desc_dct = desc_dct

        self.num_entries, self.num_entries_for, self.num_entries_per_mb, self.num_iterations = None, None, None, None
        self.events, self.event_iterator = None, None
        self.iters = 0

    def _setup_num_iterations(self):
        if self.entry_start is not None and self.entry_stop is not None:
            self.num_entries = self.entry_stop - self.entry_start

        self.num_iterations = 1 + self.num_entries // self.num_entries_for

    def get_events(self, save=False):
        events = uproot.open(f"{self.root_file}:{self.postfix}" if self.postfix else self.root_file)

        self.num_entries = events.num_entries
        self.num_entries_for = events.num_entries_for(
            self.step_size,
            filter_name=self.filter_name,
            filter_branch=self.filter_branch,
        )
        self.num_entries_per_mb = self.num_entries_for / self.float_step_size

        self._setup_num_iterations()

        if save:
            self.events = events

        return events

    def get_iterator(self, save=False, **kwargs):
        if self.events is None:
            events = self.get_events()
        else:
            events = self.events

        event_iterator = events.iterate(
            step_size=self.num_entries_for,
            library="ak",
            report=True,
            filter_name=self.filter_name,
            filter_branch=self.filter_branch,
            entry_start=self.entry_start,
            entry_stop=self.entry_stop,
            **kwargs,
        )

        if save:
            self.event_iterator = event_iterator

        return event_iterator


class ROOTFileLoader:
    def __init__(
        self,
        root_files,
        name,
        postifx="NOMINAL",
        root_files_desc_dct=None,
        chunks=None,
        max_auto_chunks=None,
        dataloader_workers=None,
        workers=1,
        show_progress=False,
    ):
        """Class for loading multiple ROOT files and setting up iterators.

        Parameters
        ----------
        root_files : str or list
            Path to ROOT files or list of paths. Can also be a directory. If directory, all ROOT files will be loaded.
        name : str
            Arbitrary name for iterators connected to this loader.
        postifx : str, optional
            ROOT file postfix, by default "NOMINAL".
        root_files_desc_dct : dict, optional
            Description dictionary for additional information, by default None.
        chunks : int, optional
            Additional partitioning of iterators, by default None.
        max_auto_chunks : int, optional
            Maximum number of auto chunks. If not given will use dataloader_workers, by default None.
        dataloader_workers : int, optional
            Number of workers used by the dataloader. Needs to be provided for auto chunking, by default None.
        workers : int, optional
            Number of workers to use for loading event iterators, by default 1.
        show_progress : bool, optional
            Whether to show progress bar, by default False.

        Note
        ----
        In order to pass information about the ROOT files, a description dictionary can be provided. This dictionary
        should have the following structure: {root_file: {key: value, ...}, ...}.

        """
        if root_files_desc_dct is not None:
            for v in root_files_desc_dct.values():
                assert isinstance(v, dict), "Description dictionary must be a dictionary of dictionaries!"

        self.name = name
        self.postfix = postifx
        self.root_files_desc_dct = root_files_desc_dct
        self.chunks = chunks
        self.workers = workers
        self.show_progress = show_progress

        self.root_files = self._setup_root_files(root_files)

        logging.info("Getting sizes for all ROOT files!")

        self.root_files_sizes = self._get_root_files_sizes()
        self.total_files_size = sum(self.root_files_sizes.values())

        logging.info("Getting number of entries for all ROOT files!")

        self.root_files_num_entries = self._get_root_files_num_entries()
        self.total_num_entries = sum(self.root_files_num_entries.values())

        self._log_info()

        if chunks == "auto":
            self.root_file_chunks = self._setup_auto_chunking(max_auto_chunks, dataloader_workers)
            logging.info(f"Auto chunking setup with {list(self.root_file_chunks.values())} chunks per file!")
        else:
            self.root_file_chunks = None

        self.event_iterators = []

    def _log_info(self):
        info_str = "\n" + 15 * "=" + " info " + 15 * "="
        info_str += f"\nName: {self.name}\n"
        info_str += f"Number of ROOT files: {len(self.root_files)}\n"
        info_str += f"Total size: {self.total_files_size:.3f} GB\n"
        info_str += f"Total number of entries: {self.total_num_entries}\n"
        info_str += 36 * "="
        logging.info(info_str)

    @staticmethod
    def _setup_root_files(root_files):
        if isinstance(root_files, list):
            return root_files
        elif os.path.isfile(root_files):
            return [root_files]
        elif os.path.isdir(root_files):
            return glob.glob(f"{root_files}/*.root")
        else:
            raise ValueError("Invalid input for root files!")

    def _get_root_files_sizes(self):
        root_file_sizes = {}

        for root_file in self.root_files:
            root_file_sizes[root_file] = get_file_size(root_file)

        return root_file_sizes

    def _get_root_files_num_entries(self):
        root_file_num_entries = {}

        for root_file in self.root_files:
            root_file_num_entries[root_file] = get_num_entries(root_file, key=self.postfix)

        return root_file_num_entries

    def _setup_auto_chunking(self, max_auto_chunks, dataloader_workers):
        if dataloader_workers is None and max_auto_chunks is None:
            raise ValueError("Number of dataloader workers or max chunks must be provided for auto chunking!")

        if max_auto_chunks is not None:
            max_chunks = max_auto_chunks
        else:
            max_chunks = dataloader_workers

        max_num_entry = max(list(self.root_files_num_entries.values()))
        chunks_array = np.linspace(0, max_num_entry, max_chunks).astype(int)

        root_file_chunks = {}
        for root_file, num_entries in self.root_files_num_entries.items():
            root_file_chunks[root_file] = np.searchsorted(chunks_array, num_entries).item()

        return root_file_chunks

    def setup_iterators(self, step_size="100 MB", filter_name=None, filter_branch=None):
        for root_file in self.root_files:
            if self.root_files_desc_dct is not None:
                if "../" in root_file:
                    key_root_file = root_file.split("/")[-1]
                else:
                    key_root_file = root_file

                desc_dct = self.root_files_desc_dct[key_root_file]
            else:
                desc_dct = None

            event_iterator = ROOTEventIterator(
                root_file,
                self.name,
                step_size,
                self.postfix,
                entry_start=None,
                entry_stop=None,
                filter_name=filter_name,
                filter_branch=filter_branch,
                desc_dct=desc_dct,
            )
            self.event_iterators.append(event_iterator)

        return self.event_iterators

    def _chunk_root_iterator(self, event_iterator):
        num_entries = event_iterator.num_entries

        if self.chunks == "auto":
            chunks = self.root_file_chunks[event_iterator.root_file]
        else:
            chunks = self.chunks

        entry_chunks = [i * (num_entries // chunks) for i in range(chunks)]
        entry_chunks.append(num_entries)

        chunked_root_loaders = []

        for i in range(len(entry_chunks) - 1):
            event_iterator_copy = copy.deepcopy(event_iterator)
            event_iterator_copy.entry_start = entry_chunks[i]
            event_iterator_copy.entry_stop = entry_chunks[i + 1]
            event_iterator_copy._setup_num_iterations()  # update num_iterations to match chunk size
            chunked_root_loaders.append(event_iterator_copy)

        return chunked_root_loaders

    def _collect_root_iterators(self, event_iterators, lock, pos):
        event_iterators_dct = {}

        if lock is not None and self.show_progress:
            with lock:
                bar = tqdm(
                    total=len(event_iterators),
                    position=pos,
                    leave=True,
                    desc=f"Started process {pos} for {len(self.root_files)} files",
                )

        for event_iterator in event_iterators:
            try:
                event_iterator.get_events()
            except KeyInFileError:
                logging.debug(f"Key {event_iterator.root_file} not found! Skipping file...")
                continue

            if lock is not None and self.show_progress:
                with lock:
                    bar.update(1)
                    bar.set_description(f"{event_iterator.num_entries} entries")

            if self.chunks:
                chunked_event_iterators = self._chunk_root_iterator(event_iterator)
                for i, chunked_event_iterator in enumerate(chunked_event_iterators):
                    if chunked_event_iterator.num_entries == 0:
                        continue
                    else:
                        event_iterators_dct[f"{chunked_event_iterator.root_file}_{i}"] = chunked_event_iterator
            else:
                if event_iterator.num_entries == 0:
                    continue

                event_iterators_dct[event_iterator.root_file] = event_iterator

        return event_iterators_dct

    def _collect_root_iterators_executor(self):
        logging.info(f"Collecting ROOT iterators using {self.workers} workers!")

        if self.workers == 1 or self.workers is None:
            self.event_iterators = self._collect_root_iterators(self.event_iterators, None, None)
            return self

        jobs_split = np.array_split(self.event_iterators, self.workers)

        m = multiprocessing.Manager()
        lock = m.Lock()

        with ProcessPoolExecutor(max_workers=self.workers) as executor:
            futures = []
            for i, job in enumerate(jobs_split):
                futures.append(executor.submit(self._collect_root_iterators, job, lock, i))

        results = []
        for future in futures:
            results.append(future.result())

        self.event_iterators = {k: v for d in results for k, v in d.items()}

        return self

    def _enumerate_root_iterators(self):
        logging.info("Enumerating ROOT iterators!")

        event_iterators_dct = {}
        for i, iterator in enumerate(self.event_iterators.values()):
            event_iterators_dct[i] = iterator

        return event_iterators_dct

    def get_iterators(self):
        """Return enumerated ROOT event iterators.

        Returns
        -------
        dict
            Dictionary of enumerated ROOT event iterators: {iter_count: ROOTEventIterator object, ...}.
        """
        self._collect_root_iterators_executor()
        event_iterators_dct = self._enumerate_root_iterators()
        return event_iterators_dct


class ROOTLoaderGenerator:
    def __init__(self, event_iterators_dct, worker_id, processors=None, heartbeats=None):
        """Internal generator class for handling ROOT event iterators and batch processing.

        Parameters
        ----------
        event_iterators_dct : dict
            Dictionary of enumerated ROOT event iterators.
        worker_id : int
            Worker ID provided by torch.
        processors : ProcessorsGraph object or list of __call__ objects, optional
            Processors graph to apply to each batch, by default None.
        heartbeats : tuple or None
            Tuple of WorkerHeartbeat objects for iterator and processor logging.
        """
        self.event_iterators_dct = event_iterators_dct
        self.worker_id = worker_id
        self.processors = processors

        if heartbeats is not None:
            self._iterator_heartbeat, self._processor_heartbeat = heartbeats
        else:
            self._iterator_heartbeat, self._processor_heartbeat = None, None

        self.heartbeats = heartbeats

        if self.processors is not None:
            if self.processors is list:
                for processor in self.processors:
                    processor.worker_id = worker_id
            else:
                for processor in self.processors.processors.values():
                    processor.worker_id = worker_id

        self.iters = 0

        logging.debug(f"Setup generator for worker id {self.worker_id} with {len(self.event_iterators_dct)} iterators!")

    def _exhaust_iterator(self, event_iterator_worker):
        event_iterator = event_iterator_worker.get_iterator()

        iters, iter_out_lst = 0, []
        while True:
            try:
                iter_out = next(event_iterator)
            except StopIteration:
                logging.debug(f"Finished iteration for {os.path.basename(event_iterator_worker.root_file)}!")
                self.iters += 1
                break

            iter_out_lst.append(iter_out)

            if self.heartbeats:
                iter_size = len(iter_out[0])
                self._iterator_heartbeat.write_heartbeat(
                    [iters, iter_size, iter_size / event_iterator_worker.num_entries_per_mb]
                )
            iters += 1

        return iter_out_lst

    def _make_report(self, event_iterator, report):
        file_path = report._source._file._file_path
        file_name = os.path.basename(file_path)
        start, stop = report._tree_entry_start, report._tree_entry_stop

        report_dct = {
            "worker_id": self.worker_id,
            "file": file_name,
            "start": start,
            "stop": stop,
            "num_entries": event_iterator.num_entries,
            "current_iter": event_iterator.iters,
            "num_iter": event_iterator.num_iterations,
        }

        report_dct = report_dct | event_iterator.desc_dct

        return report_dct

    def _parse_iterator_results(self, event_iterator_worker, iter_out_lst):
        arrays_lst, report_lst = [], []

        for iter_out in iter_out_lst:
            arrays, report = iter_out
            report_dct = self._make_report(event_iterator_worker, report)
            arrays_lst.append(arrays)
            report_lst.append(report_dct)

        arrays = ak.concatenate(arrays_lst)

        return arrays, report_lst

    def _run_processors(self, event_iterator_worker, arrays, reports):
        if self.processors is None:
            return arrays, reports
        elif self.processors is list:
            for proc in self.processors:
                arrays, reports = proc(arrays, reports, event_iterator_worker)
            return arrays, reports
        else:
            processors = self.processors.fit(arrays, reports, event_iterator_worker)
            return processors

    def __iter__(self):
        return self

    def __next__(self):
        try:
            event_iterator_worker = self.event_iterators_dct[self.iters]
        except KeyError:
            raise StopIteration

        if self.heartbeats:
            self._iterator_heartbeat.open()

        iter_worker_results = self._exhaust_iterator(event_iterator_worker)
        arrays, reports = self._parse_iterator_results(event_iterator_worker, iter_worker_results)

        if self.heartbeats:
            self._iterator_heartbeat.close()

            self._processor_heartbeat.open()
            processor_run_start = get_ms_time()

        iter_out = self._run_processors(event_iterator_worker, arrays, reports)

        if self.heartbeats:
            self._processor_heartbeat.write_heartbeat([get_ms_time() - processor_run_start, len(arrays), len(reports)])
            self._processor_heartbeat.close()

        logging.debug(f"Yield from {self}.")
        return iter_out


class ROOTIterableDataset(IterableDataset):
    def __init__(
        self,
        event_iterators_dct,
        num_workers,
        run_name="",
        processors=None,
        sharding_strategy="random",
        worker_logger=None,
        monitor=False,
    ):
        """Torch iterable style dataset for ROOT event iterators.

        Parameters
        ----------
        event_iterators_dct : dict
            Dictionary of enumerated ROOT event iterators.
        num_workers : int
            Number of workers to use for loading event iterators.
        run_name : str, optional
            Name of the run, by default "".
        processors : ProcessorsGraph object or list of __call__ objects, optional
            Processors graph to apply to each batch, by default None.
        sharding_strategy : str, optional
            Strategy for sharding (splitting) event iterators, by default "uniform".
        worker_logger : WorkerLogger object, optional
            Worker logger object for logging worker information, by default None.
        monitor : bool, optional
            Flag to enable monitoring, by default False. If True will turn on monitoring.

        References
        ----------
        [1] - https://pytorch.org/docs/stable/data.html#torch.utils.data.IterableDataset

        """
        self.event_iterators_dct, self.num_workers = event_iterators_dct, num_workers
        self.run_name = run_name
        self.processors = processors
        self.worker_logger = worker_logger
        self.monitor = monitor

        assert sharding_strategy in ["uniform", "random"], "Invalid sharding strategy!"

        if sharding_strategy == "uniform":
            self._sharding_idx = np.arange(len(event_iterators_dct))
        else:
            self._sharding_idx = np.random.permutation(len(event_iterators_dct))

        self.start_time = get_ms_time()

    def _init_heartbeats(self, worker_id):
        iterator_heartbeat = WorkerHeartbeat(
            worker_id,
            run_name=self.run_name,
            prefix="iterator",
            fields=["iterations", "events", "size"],
        )
        processor_heartbeat = WorkerHeartbeat(
            worker_id,
            run_name=self.run_name,
            prefix="processor",
            fields=["run_time", "start_n", "start_iters"],
        )
        return iterator_heartbeat, processor_heartbeat

    def __iter__(self):
        worker_info = torch.utils.data.get_worker_info()
        worker_id = worker_info.id

        if self.monitor:
            heartbeats = self._init_heartbeats(worker_id)
        else:
            heartbeats = None

        if worker_info is None:
            logging.info("Using single-process loading!")
            return ROOTLoaderGenerator(
                self.event_iterators_dct,
                0,
                processors=self.processors,
                heartbeats=heartbeats,
            )

        event_iterators = np.array([i for i in self.event_iterators_dct.values()])

        worker_shard = self._sharding_idx[worker_id :: self.num_workers]
        event_iterators_shard = event_iterators[worker_shard]

        worker_dct = {i: v for i, v in enumerate(event_iterators_shard)}

        if self.monitor and self.worker_logger is not None:
            self.worker_logger(worker_dct, worker_id, self.start_time)

        return ROOTLoaderGenerator(
            worker_dct,
            worker_id,
            processors=self.processors,
            heartbeats=heartbeats,
        )


def get_root_dataloader(
    root_files,
    name,
    chunks=None,
    max_auto_chunks=None,
    setup_workers=1,
    step_size="100 MB",
    postifx="NOMINAL",
    filter_name=None,
    filter_branch=None,
    root_files_desc_dct=None,
    processors=None,
    run_name="root_dl",
    monitor=False,
    num_workers=0,
    prefetch_factor=None,
    **kwargs,
):
    """Utility function for setting up ROOT dataloader.

    Returns
    -------
    DataLoader
        PyTorch DataLoader object.
    int
        Total number of entries.

    References
    ----------
    [1] - https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader

    """
    max_workers = multiprocessing.cpu_count()

    if setup_workers == -1:
        setup_workers = max_workers

    if num_workers == -1:
        num_workers = max_workers

    if run_name is None:
        run_name = "root_dataloader_{:%Y-%m-%d_%H-%M-%S}".format(datetime.datetime.now())

    if os.path.exists(f"logs/{run_name}"):
        logging.info(f"Directory logs/{run_name} already exists! Overwriting...")
        for f in glob.glob(f"logs/{run_name}/*"):
            os.system(f"rm -rf {f}")

    if monitor:
        logging.info("[yellow]Monitoring enabled![/yellow]")

    root_file_loader = ROOTFileLoader(
        root_files=root_files,
        name=name,
        postifx=postifx,
        root_files_desc_dct=root_files_desc_dct,
        chunks=chunks,
        max_auto_chunks=max_auto_chunks,
        dataloader_workers=num_workers,
        workers=setup_workers,
        show_progress=False,
    )
    root_file_loader.setup_iterators(
        step_size=step_size,
        filter_name=filter_name,
        filter_branch=filter_branch,
    )
    event_iterators_dct = root_file_loader.get_iterators()

    root_dataset = ROOTIterableDataset(
        event_iterators_dct,
        num_workers,
        run_name=run_name,
        processors=processors,
        worker_logger=WorkerLogger(num_workers, run_name=run_name),
        monitor=monitor,
    )

    root_dataloader = DataLoader(
        root_dataset,
        batch_size=None,
        num_workers=num_workers,
        prefetch_factor=prefetch_factor,
        **kwargs,
    )

    return root_dataloader, root_file_loader.total_num_entries
