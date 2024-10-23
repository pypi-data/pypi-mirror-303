import logging
import os
from dataclasses import asdict, dataclass, field
from glob import glob

import numpy as np
import pandas as pd
import uproot

from f9columnar.utils.regex_helpers import (
    extract_campaign_from_file,
    extract_dsid_from_file,
    extract_user_from_file,
    extract_year_from_file,
)


@dataclass
class HistDataFile:
    file_path: str
    year: int
    file_name: str = None
    full_file_name: str = None
    is_data: bool = True

    def __post_init__(self):
        self.file_name = self.file_path.split("/")[-1].split(".")[3]
        self.full_file_name = ".".join(self.file_path.split("/")[-1].split(".")[:-2])

    def __str__(self):
        return f"HistDataFile(name={self.file_name}, year={self.year})"


@dataclass
class HistMCFile:
    file_path: str
    dsid: int
    campaign: str
    file_name: str = None
    full_file_name: str = None
    is_data: bool = False

    initial_events: int = None
    initial_sow: float = None
    initial_sow_sq: float = None

    def _get_sow(self):
        with uproot.open(self.file_path) as root_file:
            for k in root_file.keys():
                if "CutBookkeeper" in k:
                    weight_key = k
                    break

            labels = root_file[weight_key].axis(0).labels()
            values = root_file[weight_key].values()

        return dict(zip(labels, values))

    def __post_init__(self):
        self.file_name = self.file_path.split("/")[-1].split(".")[3]
        self.full_file_name = ".".join(self.file_path.split("/")[-1].split(".")[:-2])

        sow_dct = self._get_sow()

        self.initial_events = sow_dct["Initial events"]
        self.initial_sow = sow_dct["Initial sum of weights"]
        self.initial_sow_sq = sow_dct["Initial sum of weights squared"]

    def __str__(self):
        return f"HistMCFile(name={self.file_name}, dsid={self.dsid}, campaign={self.campaign})"


@dataclass
class RucioHistDataset:
    dataset_path: str
    dataset_name: str = None
    full_dataset_name: str = None
    version: str = None
    user: str = None
    data: list = field(default_factory=list)

    def _setup_hist_files(self, data_file):
        dsid = extract_dsid_from_file(data_file)
        campaign = extract_campaign_from_file(data_file)
        year = extract_year_from_file(data_file)

        if dsid is None:
            h = HistDataFile(file_path=data_file, year=year)
        else:
            h = HistMCFile(file_path=data_file, dsid=dsid, campaign=campaign)

        self.data.append(h)

    def _setup_hist(self, ext="root"):
        self.full_dataset_name = ".".join(self.dataset_path.split("/")[-2].split(".")[:-1])
        self.dataset_name = self.full_dataset_name.split(".")[-1]
        self.version = self.dataset_path.split("/")[-2].split(".")[-1].split("_")[0]
        self.user = extract_user_from_file(self.dataset_path)

        self.full_dataset_name += f".{self.version}"

        data_files = glob(f"{self.dataset_path}/*.{ext}")
        assert len(data_files) > 0, "No data files found!"

        for data_file in data_files:
            if "hist-output" in data_file:
                self._setup_hist_files(data_file)
            else:
                logging.warning(f"Unknown file: {data_file}")

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f"RucioHistDataset(name={self.dataset_name}, version={self.version}, num. datasets={len(self)})"

    def __post_init__(self):
        self._setup_hist()


class RucioDB:
    def __init__(self, data_path=None):
        if data_path is not None:
            self.data_path = data_path
        else:
            self.data_path = os.environ.get("DATA_PATH", None)

        assert self.data_path is not None, "DATA_PATH not set!"

        self.datasets, self.df_id, self.rucio_db = [], None, None

    def build_hists(self, hists_dir="hists"):
        hists_path = f"{self.data_path}/{hists_dir}"
        hists_dirs = glob(f"{hists_path}/*/", recursive=True)

        for dataset_path in hists_dirs:
            ds = RucioHistDataset(dataset_path=dataset_path)
            self.datasets.append(ds)

        self.df_id = "hist"

        return self

    def to_dataframe(self, df_id=None, save=True, force=False, latest=True):
        if df_id is None:
            df_id = self.df_id

        assert df_id is not None, "df_id not set!"

        csv_path = f"{self.data_path}/rucio_{df_id}_df.csv"

        if not force and os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            df = df.replace({"NULL": np.nan})
            self.rucio_db = df
            return self.rucio_db

        assert len(self.datasets) > 0, "No datasets found!"
        df_lst = []

        for dataset in self.datasets:
            dataset_dct = asdict(dataset)
            dataset_data_dct = dataset_dct.pop("data")
            dataset_dct.pop("dataset_path", None)

            for data_dct in dataset_data_dct:
                data_dct.pop("file_path", None)
                df_lst.append({**dataset_dct, **data_dct})

        self.rucio_db = pd.DataFrame(df_lst)

        if latest:
            dataset_names, dfs = self.rucio_db["dataset_name"].unique(), []

            for dataset_name in dataset_names:
                versions = self.rucio_db[self.rucio_db["dataset_name"] == dataset_name]["version"].unique()
                keep_version = versions[-1]
                dfs.append(
                    self.rucio_db[
                        (self.rucio_db["dataset_name"] == dataset_name) & (self.rucio_db["version"] == keep_version)
                    ]
                )

            self.rucio_db = pd.concat(dfs)

        if save:
            self.rucio_db.to_csv(csv_path, index=False, sep=",", na_rep="NULL")

        return self.rucio_db

    def __len__(self):
        return len(self.datasets)

    def __call__(self, *args, **kwargs):
        return self.to_dataframe(*args, **kwargs)
