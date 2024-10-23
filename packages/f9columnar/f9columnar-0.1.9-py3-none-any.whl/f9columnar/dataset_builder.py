import copy
import logging
import os
from abc import ABC, abstractmethod

import pandas as pd

from f9columnar.hdf5_dataloader import get_hdf5_dataloader
from f9columnar.root_dataloader import get_root_dataloader
from f9columnar.utils.config_utils import apply_config_to_db
from f9columnar.utils.rucio_db import RucioDB
from f9columnar.utils.rucio_utils import make_rucio_url
from f9columnar.utils.xsec_db import XsecDB


class PhysicsDataset(ABC):
    def __init__(self, name, is_data):
        self.name = name
        self.is_data = is_data

        self.file_desc_dct = None
        self.dataloader_config, self.dataloader, self.num_entries = None, None, None

    @abstractmethod
    def _setup_file_desc_dct(self):
        pop_attrs = ["dataloader", "num_entries", "file_desc_dct"]

        desc_dct = copy.deepcopy(self.__dict__)
        for attr in pop_attrs:
            desc_dct.pop(attr, None)

        return desc_dct

    @abstractmethod
    def setup_dataloader(self, **kwargs):
        pass

    @abstractmethod
    def init_dataloader(self, processors=None):
        pass


class HDF5PhysicsDataset(PhysicsDataset):
    def __init__(self, name, file_path, is_data):
        super().__init__(name, is_data=is_data)
        self.file_path = file_path

        self.dataset_name = "data" if is_data else "mc"

        self.file_desc_dct = None
        self.dataloader_config, self.dataloader, self.num_entries = None, None, None

    def _setup_file_desc_dct(self):
        pop_attrs = ["dataloader", "num_entries", "hdf_file_desc_dct"]

        dct = copy.deepcopy(self.__dict__)
        for attr in pop_attrs:
            dct.pop(attr, None)

        return dct

    def setup_dataloader(self, **kwargs):
        assert "processors" not in kwargs, "Processors should not be passed in setup_dataloader!"
        self.dataloader_config = kwargs

        self.file_desc_dct = self._setup_file_desc_dct()

        return self

    def init_dataloader(self, processors=None):
        self.dataloader, self.num_entries = get_hdf5_dataloader(
            self.file_path,
            self.dataset_name,
            desc_dct=self.file_desc_dct,
            processors=processors,
            **self.dataloader_config,
        )
        return self


class NtuplePhysicsDataset(PhysicsDataset):
    def __init__(self, name, is_data, dataset_selection):
        super().__init__(name, is_data=is_data)
        self.dataset_selection = dataset_selection

    def _setup_file_desc_dct(self):
        pop_attrs = ["dataloader", "num_entries", "file_desc_dct"]
        file_desc_dct = {}

        root_files = self.dataset_selection["root_file"]

        for root_file in root_files:
            dct = copy.deepcopy(self.__dict__)

            for attr in pop_attrs:
                dct.pop(attr, None)

            file_desc_dct[root_file] = dct

        return file_desc_dct

    def setup_dataloader(self, **kwargs):
        assert "processors" not in kwargs, "Processors should not be passed in setup_dataloader!"

        self.dataloader_config = kwargs

        if self.file_desc_dct is None:
            self.file_desc_dct = self._setup_file_desc_dct()

        return self

    def init_dataloader(self, processors=None):
        root_files = self.dataset_selection["root_file"].tolist()

        self.dataloader, self.num_entries = get_root_dataloader(
            root_files,
            self.name,
            root_files_desc_dct=self.file_desc_dct,
            processors=processors,
            **self.dataloader_config,
        )

        return self


class NtupleMCDataset(NtuplePhysicsDataset):
    def __init__(self, name, dataset_selection, use_weights=True):
        super().__init__(name=name, dataset_selection=dataset_selection, is_data=False)
        self.use_weights = use_weights

        if use_weights:
            self.sample_weights = self._setup_weights()
        else:
            self.sample_weights = None

    def _setup_weights(self):
        root_files = self.dataset_selection["root_file"]
        eff_xsecs = self.dataset_selection["eff_xsec"]

        sample_weights = {}

        for root_file, eff_xsec in zip(root_files, eff_xsecs):
            sample_weights[os.path.basename(root_file)] = eff_xsec

        return sample_weights

    def __str__(self):
        return f"NtupleMCDataset(name={self.name})"


class NtupleDataDataset(NtuplePhysicsDataset):
    def __init__(self, name, dataset_selection):
        super().__init__(name=name, dataset_selection=dataset_selection, is_data=True)

    def __str__(self):
        return f"NtupleDataDataset(name={self.name})"


class NtupleMergedPhysicsDataset:
    def __init__(self, name, datasets, is_data):
        self.name = name
        self.datasets = datasets
        self.is_data = is_data

        self.dataset_selection, self.file_desc_dct = [], {}
        self.dataloader_config, self.dataloader, self.num_entries = None, None, None

    def merge(self):
        dataloader_configs = []

        for dataset in self.datasets:
            dataloader_configs.append(dataset.dataloader_config)
            self.dataset_selection.append(dataset.dataset_selection)

            self.file_desc_dct.update(dataset.file_desc_dct)

        logging.info(f"[green]Merged {len(self.datasets)} datasets into {self.name} dataset![/green]")

        self.dataloader_config = dataloader_configs[0]
        logging.info("Using first dataloader config.")

        return self

    def init_dataloader(self, processors=None):
        dataset_selection = pd.concat(self.dataset_selection)
        root_files = dataset_selection["root_file"].tolist()

        self.dataloader, self.num_entries = get_root_dataloader(
            root_files,
            self.name,
            root_files_desc_dct=self.file_desc_dct,
            processors=processors,
            **self.dataloader_config,
        )
        return self


class DatasetBuilder(ABC):
    def __init__(self, data_path=None):
        if data_path is not None:
            self.data_path = data_path
        else:
            self.data_path = os.environ.get("DATA_PATH", None)

        assert self.data_path is not None, "DATA_PATH not set!"

    @abstractmethod
    def build_mc_datasets(self):
        """Build MC datasets. Returns a list of MCDataset instances."""
        pass

    @abstractmethod
    def build_data_datasets(self):
        """Build data datasets. Returns a list of DataDataset instances."""
        pass

    @abstractmethod
    def setup_dataloaders(self, dataloader_config=None):
        """Setup dataloaders for MC and data datasets."""
        pass

    @abstractmethod
    def init_dataloaders(self, processors=None):
        """Initialize dataloaders for MC and data datasets."""
        pass

    @abstractmethod
    def build(self, dataloader_config=None):
        """Build datasets, setup dataloaders and initialize dataloaders."""
        pass

    @abstractmethod
    def init(self, processors=None):
        """Initialize dataloaders."""
        pass


class NtupleDatasetBuilder(DatasetBuilder):
    def __init__(
        self,
        config_name=None,
        data_path=None,
        ntuple_location=None,
        max_root_files=None,
        pmg_mc="mc16",
        df_id="hist",
    ):
        super().__init__(data_path=data_path)

        if ntuple_location is not None:
            self.ntuple_location = ntuple_location
        else:
            self.ntuple_location = os.environ.get("NTUPLE_LOCATION", None)

        assert self.ntuple_location is not None, "NTUPLE_LOCATION not set!"

        self.rucio_db = RucioDB(data_path=self.data_path)(df_id)

        if config_name:
            self.rucio_db = apply_config_to_db(config_name, self.rucio_db)

        self.max_root_files = max_root_files
        self.xsec_db = XsecDB(pmg_mc)()
        self.mc_datasets, self.data_datasets = [], []

    def _make_root_files(self, files, users=None, return_base_files=False):
        root_base_files = [f"{f}.tree.root" for f in files]

        if self.ntuple_location == "rucio":
            root_files = []

            for user, root_file in zip(users, root_base_files):
                root_files.append(make_rucio_url(user, root_file))
        else:
            root_files = [os.path.join(self.ntuple_location, root_file) for root_file in root_base_files]

        if return_base_files:
            return root_files, root_base_files
        else:
            return root_files

    def _split_for_max_root_files(self, df):
        split_df = []

        for i in range(len(df) // self.max_root_files + 1):
            split = df[i * self.max_root_files : (i + 1) * self.max_root_files]
            if len(split) != 0:
                split_df.append(split)

        return split_df

    def build_mc_datasets(self):
        logging.info("[green]Building MC datasets![/green]")

        mc_df = self.rucio_db[self.rucio_db["is_data"] == False]

        dataset_names = mc_df["dataset_name"].unique()

        mc_datasets = []
        for dataset_name in dataset_names:
            dataset_selection = mc_df[mc_df["dataset_name"] == dataset_name].copy()

            full_file_names = dataset_selection["full_file_name"]
            users = dataset_selection["user"]

            dataset_selection["root_file"] = self._make_root_files(full_file_names, users)

            dsids = dataset_selection["dsid"].astype(int).tolist()
            eff_xsecs = []

            for dsid in dsids:
                eff_xsec = self.xsec_db[self.xsec_db["dataset_number"] == dsid]["effectiveCrossSection"]
                eff_xsecs.append(eff_xsec.values[0])

            dataset_selection["eff_xsec"] = eff_xsecs

            if self.max_root_files is not None:
                dataset_selection = self._split_for_max_root_files(dataset_selection)
            else:
                dataset_selection = [dataset_selection]

            for i, df in enumerate(dataset_selection):
                mc_datasets.append(NtupleMCDataset(f"{dataset_name}_{i}", df, use_weights=True))

        return mc_datasets

    def build_data_datasets(self):
        logging.info("[green]Building data datasets![/green]")

        data_df = self.rucio_db[self.rucio_db["is_data"] == True]

        dataset_names = data_df["dataset_name"].unique()

        data_datasets = []
        for dataset_name in dataset_names:
            dataset_selection = data_df[data_df["dataset_name"] == dataset_name].copy()

            full_file_names = dataset_selection["full_file_name"]
            users = dataset_selection["user"]

            dataset_selection["root_file"] = self._make_root_files(full_file_names, users)

            if self.max_root_files is not None:
                dataset_selection = self._split_for_max_root_files(dataset_selection)
            else:
                dataset_selection = [dataset_selection]

            for i, df in enumerate(dataset_selection):
                data_datasets.append(NtupleDataDataset(f"{dataset_name}_{i}", df))

        return data_datasets

    def setup_dataloaders(self, dataloader_config=None):
        if dataloader_config is None:
            dataloader_config = {}

        logging.info("[green]Setting up MC dataloaders![/green]")
        for mc in self.mc_datasets:
            mc.setup_dataloader(**dataloader_config)

        logging.info("[green]Setting up data dataloaders![/green]")
        for data in self.data_datasets:
            data.setup_dataloader(**dataloader_config)

        return self

    def init_dataloaders(self, processors=None):
        logging.info("[green]Initializing MC dataloaders![/green]")
        for mc in self.mc_datasets:
            mc.init_dataloader(processors=processors)

        logging.info("[green]Initializing data dataloaders![/green]")
        for data in self.data_datasets:
            data.init_dataloader(processors=processors)

        return self

    def build(self, dataloader_config=None, merge=False):
        self.mc_datasets = self.build_mc_datasets()
        self.data_datasets = self.build_data_datasets()

        self.setup_dataloaders(dataloader_config)

        if merge:
            self.mc_datasets = [NtupleMergedPhysicsDataset("MC", self.mc_datasets, is_data=False).merge()]
            self.data_datasets = [NtupleMergedPhysicsDataset("Data", self.data_datasets, is_data=True).merge()]

        return self

    def init(self, processors=None):
        self.init_dataloaders(processors=processors)
        return self.mc_datasets, self.data_datasets
