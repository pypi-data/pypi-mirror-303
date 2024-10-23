import json
import logging
import multiprocessing

import h5py
import numpy as np
import torch
from torch.utils.data import DataLoader, IterableDataset


class HDF5LoaderGenerator:
    def __init__(self, file_path, dataset_name, chunk_size, processors, shape, chunks_idx, worker_id, desc_dct=None):
        self.file_path = file_path
        self.dataset_name = dataset_name
        self.chunk_size = chunk_size
        self.processors = processors

        self.shape = shape
        self.chunks_idx = chunks_idx
        self.worker_id = worker_id

        if desc_dct is None:
            self.desc_dct = {}
        else:
            self.desc_dct = desc_dct

        self.n_chunks = self.shape[0] // self.chunk_size + 1
        self.current_chunk_idx = 0

    def _make_report(self):
        report_dct = {
            "worker_id": self.worker_id,
            "file": self.file_path,
            "shape": self.shape,
            "n_chunks": self.n_chunks,
        }
        return report_dct | self.desc_dct

    def _load_chunk(self):
        if self.current_chunk_idx == self.n_chunks:
            raise StopIteration

        logging.debug(f"Loading chunk {self.current_chunk_idx}/{len(self.chunks_idx) - 1} on worker {self.worker_id}!")

        chunk_idx = self.chunks_idx[self.current_chunk_idx]

        with h5py.File(self.file_path, "r") as f:
            chunk_arrays = f[self.dataset_name][chunk_idx]

        self.current_chunk_idx += 1

        return chunk_arrays

    def __iter__(self):
        return self

    def __next__(self):
        chunk_arrays = self._load_chunk()
        reports = [self._make_report()]

        if self.processors is not None:
            return self.processors.fit(chunk_arrays, reports)
        else:
            return chunk_arrays, reports


class PiledHDF5LoaderGenerator:
    def __init__(self, file_path, piles_lst, processors, worker_id, desc_dct=None):
        self.file_path = file_path
        self.piles_lst = piles_lst
        self.processors = processors
        self.worker_id = worker_id

        if desc_dct is None:
            self.desc_dct = {}
        else:
            self.desc_dct = desc_dct

        self.current_pile_idx = 0
        self.current_pile = None

    def _make_report(self):
        report_dct = {
            "worker_id": self.worker_id,
            "file": self.file_path,
            "current_pile": self.current_pile,
            "current_pile_idx": self.current_pile_idx,
        }
        return report_dct | self.desc_dct

    def _load_pile(self):
        if self.current_pile_idx == len(self.piles_lst):
            raise StopIteration

        logging.debug(f"Loading pile {self.current_pile_idx}/{len(self.piles_lst) - 1} on worker {self.worker_id}!")

        pile = self.piles_lst[self.current_pile_idx]

        with h5py.File(self.file_path, "r") as f:
            pile_arrays = f[pile][:]

        self.current_pile = pile
        self.current_pile_idx += 1

        return pile_arrays

    def __iter__(self):
        return self

    def __next__(self):
        pile_arrays = self._load_pile()
        reports = [self._make_report()]

        if self.processors is not None:
            return self.processors.fit(pile_arrays, reports)
        else:
            return pile_arrays, reports


class HDF5IterableDataset(IterableDataset):
    def __init__(
        self,
        file_path,
        dataset_name,
        num_workers,
        chunk_size=None,
        use_piles=False,
        processors=None,
        desc_dct=None,
    ):
        """Create an iterable dataset from an hdf5 file. The data is split into chunks of size `chunk_size`.

        Parameters
        ----------
        file_path : str
            Path to the hdf5 file.
        dataset_name : str
            Name of the dataset in the hdf5 file.
        num_workers : int
            Number of workers to use.
        chunk_size : int
            Size of the data chunks.
        use_piles : bool, optional
            Flag to use piles, by default False.
        processors : ProcessorsGraph
            Processors graph to apply to the data.
        desc_dct : dict
            Description dictionary for additional information.
        """
        super().__init__()
        self.file_path = file_path
        self.dataset_name = dataset_name
        self.chunk_size = chunk_size
        self.num_workers = num_workers
        self.use_piles = use_piles
        self.desc_dct = desc_dct

        if self.use_piles is False and self.chunk_size is None:
            raise ValueError("chunk_size must be provided if use_piles is False!")

        self.processors = processors
        if self.processors is not None:
            self.processors.copy_processors = True

        if self.use_piles:
            self.piles_lst = self._get_metadata(self.file_path)["piles"][dataset_name]
            self.piles_shapes = self._get_shape()
            self.shape = (sum([s[0] for s in self.piles_shapes]), self.piles_shapes[0][1])
        else:
            self.shape = self._get_shape()
            self.chunks_idx = self._setup_chunks()

    def _get_metadata(self, file_path):
        with h5py.File(file_path, "r") as f:
            metadata = json.loads(f["metadata"][()])
        return metadata

    def _get_shape(self):
        with h5py.File(self.file_path, "r") as f:
            if self.use_piles:
                shape = [f[pile].shape for pile in self.piles_lst]
            else:
                shape = f[self.dataset_name].shape

        return shape

    def _setup_chunks(self):
        """Split the data in hdf5 into chunks of size `chunk_size`.

        Returns
        -------
        list of arrays
            Indices of the data chunks.
        """
        n_chunks = self.shape[0] // self.chunk_size + 1

        idx = np.arange(0, self.shape[0], 1)
        chunks_idx = np.array_split(idx, n_chunks)

        return chunks_idx

    def _iter_default(self):
        worker_info = torch.utils.data.get_worker_info()

        if worker_info is None:
            worker_id = 0
        else:
            worker_id = worker_info.id

        if len(self.chunks_idx) < self.num_workers:
            raise ValueError(f"Number of chunks ({len(self.chunks_idx)}) must be < num_workers ({self.num_workers})!")

        worker_split_chunks_idx, worker_shape_splits = [], []

        for i in range(self.num_workers):
            worker_split_chunks_idx.append(self.chunks_idx[i :: self.num_workers])
            worker_shape_splits.append((sum([s.shape[0] for s in worker_split_chunks_idx[i]]), self.shape[1]))

        return HDF5LoaderGenerator(
            self.file_path,
            self.dataset_name,
            self.chunk_size,
            self.processors,
            shape=worker_shape_splits[worker_id],
            chunks_idx=worker_split_chunks_idx[worker_id],
            worker_id=worker_id,
            desc_dct=self.desc_dct,
        )

    def _iter_piles(self):
        worker_info = torch.utils.data.get_worker_info()

        if worker_info is None:
            worker_id = 0
        else:
            worker_id = worker_info.id

        if len(self.piles_lst) < self.num_workers:
            raise ValueError(f"Number of piles ({len(self.piles_lst)}) must be < num_workers ({self.num_workers})!")

        worker_piles_split = []

        for i in range(self.num_workers):
            worker_piles_split.append(self.piles_lst[i :: self.num_workers])

        return PiledHDF5LoaderGenerator(
            self.file_path,
            piles_lst=worker_piles_split[worker_id],
            processors=self.processors,
            worker_id=worker_id,
            desc_dct=self.desc_dct,
        )

    def __iter__(self):
        if self.use_piles:
            return self._iter_piles()
        else:
            return self._iter_default()


def get_hdf5_dataloader(
    file_path,
    dataset_name,
    chunk_size=None,  # this is effectively the batch size
    use_piles=False,
    desc_dct=None,
    processors=None,
    num_workers=0,
    prefetch_factor=None,
    **kwargs,
):
    """Create a dataloader for a single hdf5 file."""
    if num_workers == -1:
        num_workers = multiprocessing.cpu_count()

    hdf5_dataset = HDF5IterableDataset(
        file_path,
        dataset_name=dataset_name,
        num_workers=num_workers,
        chunk_size=chunk_size,
        use_piles=use_piles,
        processors=processors,
        desc_dct=desc_dct,
    )

    hdf5_dataloader = DataLoader(
        hdf5_dataset,
        batch_size=None,
        num_workers=num_workers,
        prefetch_factor=prefetch_factor,
        collate_fn=lambda batch: batch,
        **kwargs,
    )

    return hdf5_dataloader, hdf5_dataset.shape[0]
