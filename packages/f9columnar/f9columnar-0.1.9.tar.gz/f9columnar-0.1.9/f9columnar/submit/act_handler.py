import glob
import logging
import os
import pickle

from f9columnar.run import EventTensorLoop
from f9columnar.utils.helpers import make_tar_file
from f9columnar.utils.rucio_utils import make_rucio_url


def job_template(
    executable,
    arguments,
    input_files,
    output_files,
    job_name,
    cpu_time=30,
    wall_time=30,
    memory=2000,
    count=1,
):
    return f"""&
(executable="{executable}")
(arguments="{arguments}")
(inputFiles={input_files})
(outputFiles={output_files})
(jobName="{job_name}")
(stdout="run.log")
(join=yes)
(gmlog="log")
(cpuTime="{cpu_time}")
(wallTime="{wall_time}")
(memory="{memory}")
(count="{count}")
(runtimeenvironment="ENV/SINGULARITY" "/cvmfs/atlas.cern.ch/repo/containers/fs/singularity/x86_64-almalinux9")"""


class ActBatchHandler:
    def __init__(
        self,
        dataset_builder,
        run_name=None,
        postprocessors=None,
        input_files=None,
        output_files=None,
        executable="run.sh",
        arccp_tar=False,
    ):
        """Class for preparing batch submission for ARC. Makes .xrsl files for submission and pickles datasets.

        Parameters
        ----------
        dataset_builder : object
            MCDdataset or DataDataset object from NtupleDatasetBuilder.
        run_name : str, optional
            String identifier for the current analysis run, by default None.
        postprocessors : object, optional
            PostprocessorsGraph, by default None. If None will be set to "run_0".
        input_files : list, optional
            List of aditional input files, by default None.
        output_files : list, optional
            List of aditional output files, by default None.
        executable : str, optional
            Name of the main run script, by default "run.sh".
        arccp_tar : bool, optional
            Flag to copy code tar file to dCache, by default False. If True need proxy.

        Note
        ----
        - Both processors and postprocessors get patched into the dataset objects for pickling.
        - Output files are set from the save_path of the postprocessors.
        - Names of the submission files are: mc_DSID_name_i.xrsl and data_year_j.xrsl and are saved in batch/run_name/.

        References
        ----------
        [1] - https://doc.vega.izum.si/arc/

        """
        self.dataset_builder = dataset_builder
        self.postprocessors = postprocessors

        if run_name is None:
            run_name = "run_0"
            logging.warning(f"Run name is not provided, using default: {run_name}")

        self.run_name = run_name
        self.batch_dir = f"batch/{run_name}"

        os.makedirs(self.batch_dir, exist_ok=True)

        if input_files is None:
            self.input_files = []
        else:
            self.input_files = input_files

        if output_files is None:
            self.output_files = []
        else:
            self.output_files = output_files

        self.executable = executable
        self.arccp_tar = arccp_tar

        self.input_files += [
            '("batch_venv.tar" "davs://dcache.sling.si:2880/atlas/jang/batch_venv.tar" "cache=invariant")',
            f'("{self.executable}" "")',
        ]

        if self.arccp_tar:
            self.input_files.append(
                '("F9Columnar.tar" "davs://dcache.sling.si:2880/atlas/jang/F9Columnar.tar" "cache=renew")'
            )
        else:
            self.input_files.append('("F9Columnar.tar" "")')

        self.output_files += self._get_output_files()

    def _get_output_files(self):
        output_files = []
        for proc in self.postprocessors.processors.values():
            f = proc.save_path

            if f is not None:
                output_files.append(os.path.basename(f))

        xrsl_output_files = "".join([f'("{f}" "")' for f in output_files])

        return [xrsl_output_files]

    def _dump(self, obj, file_name):
        with open(file_name, "wb") as f:
            pickle.dump(obj, f)

    def configure_rucio_files(self, prefix="../"):
        logging.info("Configuring rucio files.")

        datasets = self.dataset_builder.mc_datasets + self.dataset_builder.data_datasets
        input_files = {"mc": [], "data": []}

        for dataset in datasets:
            root_files, dataset_input_files = [], []
            for root_file in dataset.root_files:
                user = root_file.split(".")[1]
                rucio_root_file = make_rucio_url(user, root_file)

                root_files.append(root_file)
                dataset_input_files.append(f'("{root_file}" "{rucio_root_file}" "cache=invariant")')

            if dataset.is_data:
                input_files["data"].append(dataset_input_files)
            else:
                input_files["mc"].append(dataset_input_files)

            dataset.root_files = [f"{prefix}{f}" for f in root_files]

        return input_files

    def save_datasets(self):
        logging.info(f"Saving datasets to {self.batch_dir}.")

        datasets = self.dataset_builder.mc_datasets + self.dataset_builder.data_datasets
        saved_datasets = {"mc": [], "data": []}

        data_count, mc_count = 0, 0
        for dataset in datasets:
            dataset.processors = self.dataset_builder.processors
            dataset.postprocessors = self.postprocessors

            if dataset.is_data:
                try:
                    name = f"data{dataset.year}_{data_count}"
                except AttributeError:
                    name = f"data_{data_count}"

                data_count += 1
            else:
                try:
                    name = f"{dataset.campaign}_{dataset.dsid}_{dataset.name}_{mc_count}"
                except AttributeError:
                    name = f"mc16_{mc_count}"

                mc_count += 1

            self._dump(dataset, f"{self.batch_dir}/{name}_dataset.p")

            if dataset.is_data:
                saved_datasets["data"].append(f'("{self.batch_dir}/{name}_dataset.p" "")')
            else:
                saved_datasets["mc"].append(f'("{self.batch_dir}/{name}_dataset.p" "")')

        return saved_datasets

    def _save_job(self, job_name, job_str):
        with open(f"{self.batch_dir}/{job_name}.xrsl", "w") as f:
            f.write(job_str)

    def make_submission_xrsl(self, input_files, saved_datasets):
        logging.info("Making submission xrsl files.")

        for i, (mc_input_files, mc_saved_dataset) in enumerate(zip(input_files["mc"], saved_datasets["mc"])):
            mc_dataset = self.dataset_builder.mc_datasets[i]

            job_input_files = "".join(self.input_files) + mc_saved_dataset + "".join(mc_input_files)
            job_output_files = "".join(self.output_files) + f'("{mc_saved_dataset.split("/")[-1]}'

            try:
                job_name = f"mc16_{mc_dataset.dsid}_{mc_dataset.name}_{i}"
            except AttributeError:
                job_name = f"mc_{i}"

            job = job_template(self.executable, self.run_name, job_input_files, job_output_files, job_name)

            self._save_job(job_name, job)

        for i, (data_input_files, data_saved_dataset) in enumerate(zip(input_files["data"], saved_datasets["data"])):
            data_dataset = self.dataset_builder.data_datasets[i]

            job_input_files = "".join(self.input_files) + data_saved_dataset + "".join(data_input_files)
            job_output_files = "".join(self.output_files) + f'("{data_saved_dataset.split("/")[-1]}'

            try:
                job_name = f"data{data_dataset.year}_{i}"
            except AttributeError:
                job_name = f"data_{i}"

            job = job_template(self.executable, self.run_name, job_input_files, job_output_files, job_name)

            self._save_job(job_name, job)

        return self

    def make_code_tar(self, exclude, include):
        logging.info("Making code tar file.")
        make_tar_file(exclude=exclude, include=include)

        if self.arccp_tar:
            logging.info("Copying tar file to dCache.")
            os.system("arccp -f F9Columnar.tar davs://dcache.sling.si:2880/atlas/jang/")
        else:
            logging.info("Using local tar file.")

    def prepare(self, exclude=None, include=None):
        logging.info("[green]Preparing batch submission![/green]")

        input_files = self.configure_rucio_files()
        saved_datasets = self.save_datasets()
        self.make_submission_xrsl(input_files, saved_datasets)
        self.make_code_tar(exclude, include)

    def __call__(self, *args, **kwargs):
        self.prepare(*args, **kwargs)


class ActBatchRunner:
    def __init__(self, run_name, save_dir="out"):
        """Class for running batch jobs on clusters. Runs the EventTensorLoop using pickled datasets.

        Parameters
        ----------
        run_name : str
            Name of the current run.
        save_dir : str, optional
            Name of the directory with outputs, by default "out".
        """
        self.run_name = run_name
        os.makedirs(save_dir, exist_ok=True)
        self.save_dir = save_dir

        self.mc_dataset, self.data_dataset = None, None
        self.postprocessors, self.event_loop = None, None

    def _load(self, file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)

    def init(self):
        dataset_files = glob.glob(f"../batch/{self.run_name}/*_dataset.p")

        assert len(dataset_files) > 0, "No datasets found!"

        for dataset_file in dataset_files:
            if "mc" in dataset_file:
                self.mc_dataset = self._load(dataset_file)
            elif "data" in dataset_file:
                self.data_dataset = self._load(dataset_file)
            else:
                pass

        if self.mc_dataset is not None:
            self.mc_dataset.init_dataloader(processors=self.mc_dataset.processors)
            self.postprocessors = self.mc_dataset.postprocessors

        if self.data_dataset is not None:
            self.data_dataset.init_dataloader(processors=self.data_dataset.processors)
            self.postprocessors = self.data_dataset.postprocessors

        return self

    def run(self):
        assert self.mc_dataset is not None or self.data_dataset is not None, "No datasets!"

        self.event_loop = EventTensorLoop(
            mc_datasets=[self.mc_dataset],
            data_datasets=[self.data_dataset],
            postprocessors_graph=self.postprocessors,
            fit_postprocessors=True,
        )

        if self.mc_dataset is None:
            data_only = True
        else:
            data_only = False

        if self.data_dataset is None:
            mc_only = True
        else:
            mc_only = False

        self.event_loop.run(mc_only=mc_only, data_only=data_only)

        return self
