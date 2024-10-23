import copy
import json
import logging

import awkward as ak
import h5py
import numpy as np

from f9columnar.processors import Postprocessor


class HDF5Writer(Postprocessor):
    def __init__(self, file_path, dataset_names=None, n_piles=None, name="hdf5_writer"):
        """HDF5 data writer postprocessor.

        Parameters
        ----------
        file_path : str
            Path to the created HDF5 file.
        dataset_names : str or list, optional
            Names of the datasets to be created. Can be dir/subdir/.../dataset_name, by default None.
        n_piles : int, optional
            Number of piles to split the data into. If provided, data will be saved to piles, by default None.
        name : str, optional
            Name of the processor, by default "hdf5_writer".

        Other Parameters
        ----------------
        shape, chunks, maxshape, dtype, compression, compression_opts
            See [1].

        Note
        ----
        A pile is a separate dataset in the HDF5 file. Each chunk of data is saved to a random pile.

        References
        ----------
        [1] - https://docs.h5py.org/en/stable/high/group.html#h5py.Group.create_dataset
        [2] - https://docs.h5py.org/en/stable/high/dataset.html
        [3] - https://pythonforthelab.com/blog/how-to-use-hdf5-files-in-python/
        [4] - https://blog.janestreet.com/how-to-shuffle-a-big-dataset/

        """
        super().__init__(name=name)
        self.file_path = file_path
        self.dataset_names = dataset_names
        self.n_piles = n_piles

        self._current_idx, self._current_shape = 0, None

        self.pile_datasets_lst, self.pile_datasets_dct, self.piles_info_dct = [], {}, {}

        if self.n_piles is not None:
            assert dataset_names is not None, "Dataset names must be provided for piles!"

            self.get_pile_dataset_names()
            self.get_piles_info(start_dct={"current_idx": 0, "current_shape": None})

    def get_pile_dataset_names(self):
        for dataset_name in self.dataset_names:
            piles = [f"{dataset_name}/p{i}" for i in range(self.n_piles)]

            self.pile_datasets_lst += piles
            self.pile_datasets_dct[dataset_name] = piles

        return self.pile_datasets_lst, self.pile_datasets_dct

    def get_piles_info(self, start_dct):
        for dataset_name, pile_names in self.pile_datasets_dct.items():
            info_dct = {}

            for pile_name in pile_names:
                info_dct[pile_name] = copy.deepcopy(start_dct)

            self.piles_info_dct[dataset_name] = info_dct

        return self.piles_info_dct

    def create_datasets(
        self,
        mode="w",
        dataset_names=None,
        shape=None,
        chunks=None,
        maxshape=None,
        dtype="float32",
        compression="gzip",
        compression_opts=4,
    ):
        assert mode in ["w", "a"], "Mode must be 'w' or 'a'!"

        if maxshape is not None:
            assert shape is not None, "Shape must be provided if maxshape is provided!"

        # auto-chunking is enabled by default, if you use compression or maxshape
        if maxshape or compression and chunks is None:
            chunks = True

        if dataset_names is None:
            dataset_names = self.dataset_names

        with h5py.File(self.file_path, mode) as f:
            for dataset_name in dataset_names:
                dataset_name_split = dataset_name.split("/")

                f_obj = f
                for i, group in enumerate(dataset_name_split):
                    if i == len(dataset_name_split) - 1:
                        f_obj.create_dataset(
                            group,
                            shape=shape,
                            chunks=chunks,
                            maxshape=maxshape,
                            dtype=dtype,
                            compression=compression,
                            compression_opts=compression_opts,
                        )
                    elif i == 0:
                        if group not in f_obj:
                            g = f.create_group(group)
                            f_obj = g
                        else:
                            f_obj = f_obj[group]
                    else:
                        g = g.create_group(group)
                        f_obj = g

    def create_pile_datasets(self, *args, **kwargs):
        assert "dataset_names" not in kwargs, "dataset_names should not be provided!"
        return self.create_datasets(*args, dataset_names=self.pile_datasets_lst, **kwargs)

    def add_data(self, data, dataset_name, idx, resize=None):
        assert type(idx) in [tuple, list], "idx must be a tuple or a list!"
        assert len(idx) <= 2, "Only support 2D data!"

        with h5py.File(self.file_path, "a") as f:
            dataset = f[dataset_name]

            if resize:
                dataset.resize(resize)

            if len(idx) == 1:
                dataset[idx] = data
            else:
                dataset[idx[0] : idx[1]] = data

    def add_metadata(self, metadata_dct, group_name=None):
        with h5py.File(self.file_path, "a") as f:
            if group_name is not None:
                group = f[group_name]
            else:
                group = f

            group.create_dataset("metadata", data=json.dumps(metadata_dct))

    def get_metadata(self, group_name=None):
        if group_name is None:
            group_name = "metadata"
        else:
            group_name = f"{group_name}/metadata"

        with h5py.File(self.file_path, "r") as f:
            metadata = json.loads(f[group_name][()])

        return metadata

    def keys(self):
        with h5py.File(self.file_path, "r") as f:
            keys = list(f.keys())

        return keys

    def get_handle(self):
        f = h5py.File(self.file_path, "r")
        return f

    def run_default(self, arrays, dataset_name, chunk_shape=1000, column_names=None):
        if self._current_shape is None:
            self._current_shape = chunk_shape

        save_arrays = []

        if column_names is None:
            column_names = arrays.fields

        for column_name in column_names:
            if column_name not in arrays.fields:
                continue

            column = ak.to_numpy(arrays[column_name])
            column = column[:, None]
            save_arrays.append(column)

        save_arrays = np.concatenate(save_arrays, axis=1)

        array_chunks = len(save_arrays) // chunk_shape + 1
        chunk_save_arrays = np.array_split(save_arrays, array_chunks)

        for chunk_array in chunk_save_arrays:
            n_chunk = len(chunk_array)
            start_idx, stop_idx = self._current_idx, self._current_idx + n_chunk

            self._current_idx = stop_idx

            if self._current_idx > self._current_shape:
                resize = (stop_idx, chunk_array.shape[1])
                self._current_shape = stop_idx
            else:
                resize = None

            self.add_data(chunk_array, dataset_name, idx=(start_idx, stop_idx), resize=resize)

        return {"arrays": arrays}

    def run_piles(self, arrays, dataset_name, chunk_shape=1000, column_names=None):
        pile_idx = np.random.choice(self.n_piles)
        pile_name = self.pile_datasets_dct[dataset_name][pile_idx]

        if self._current_shape is None:
            self._current_shape = chunk_shape

        save_arrays = []

        if column_names is None:
            column_names = arrays.fields

        for column_name in column_names:
            if column_name not in arrays.fields:
                continue

            column = ak.to_numpy(arrays[column_name])
            column = column[:, None]
            save_arrays.append(column)

        save_arrays = np.concatenate(save_arrays, axis=1)

        array_chunks = len(save_arrays) // chunk_shape + 1
        chunk_save_arrays = np.array_split(save_arrays, array_chunks)

        for chunk_array in chunk_save_arrays:
            n_chunk = len(chunk_array)

            start_idx = self.piles_info_dct[dataset_name][pile_name]["current_idx"]
            stop_idx = start_idx + n_chunk

            self.piles_info_dct[dataset_name][pile_name]["current_idx"] = stop_idx

            if (
                self.piles_info_dct[dataset_name][pile_name]["current_idx"]
                > self.piles_info_dct[dataset_name][pile_name]["current_shape"]
            ):
                resize = (stop_idx, chunk_array.shape[1])
                self.piles_info_dct[dataset_name][pile_name]["current_shape"] = stop_idx
            else:
                resize = None

            self.add_data(chunk_array, pile_name, idx=(start_idx, stop_idx), resize=resize)

        return {"arrays": arrays}

    def run(self, arrays, *args, **kwargs):
        if self.n_piles is None:
            return self.run_default(arrays, *args, **kwargs)
        else:
            return self.run_piles(arrays, *args, **kwargs)


class NtupleHDF5Writer(HDF5Writer):
    def __init__(
        self,
        file_path,
        column_names,
        n_piles=None,
        mc_only_column_names=None,
        chunk_shape=1000,
        mc_labels=None,
        save_node="output",
        write_mc=True,
        write_data=True,
        hdf5_kwargs=None,
    ):
        """Ntuple HDF5 data writer postprocessor. Saves selected columns to the HDF5 file in a matrix form.

        Parameters
        ----------
        file_path : str
            Path to the created HDF5 file.
        column_names : list
            List of column names (variables) to be saved from arrays.
        n_piles : int, optional
            Number of piles to split the data into, by default None.
        mc_only_column_names : list, optional
            List of columns that are only in MC arrays, by default None.
        chunk_shape : int, optional
            Number of rows to save in one chunk, by default 1000.
        mc_labels : list, optional
            Names of the MC datasets (additional columns with 0 and 1), by default None.
        save_node : str, optional
            Name of the node in the processors graph to save arrays from, by default "output".
        write_mc : bool, optional
            Write MC arrays to the HDF5 file, by default True.
        write_data : bool, optional
            Write data arrays to the HDF5 file, by default True.
        hdf5_kwargs : dict, optional
            Additional arguments for the HDF5 writer create_datasets method, by default None.

        Note
        ----
        Variable names should be saved in metadata in the correct order they come in the matrix columns.

        """
        super().__init__(file_path, dataset_names=["data", "mc"], n_piles=n_piles, name="ntuple_hdf5_writer")

        self.column_names = column_names
        self.mc_only_column_names = [] if mc_only_column_names is None else mc_only_column_names
        self.chunk_shape = chunk_shape
        self.mc_labels = mc_labels
        self.save_node = save_node

        assert write_mc or write_data, "At least one of write_mc or write_data must be True!"
        self.write_mc, self.write_data = write_mc, write_data

        self.hdf5_kwargs = {} if hdf5_kwargs is None else hdf5_kwargs

        self._current_shape = chunk_shape
        self._current_is_data = False

        if self.n_piles:
            self.get_piles_info(start_dct={"current_idx": 0, "current_shape": chunk_shape})

        self.create_ntuple_datasets()

    def create_ntuple_datasets(self):
        logging.info("Creating hdf5 ntuple datasets!")

        metadata = {}

        if self.mc_labels:
            shape = (self.chunk_shape, len(self.column_names) + len(self.mc_labels))
            maxshape = (None, len(self.column_names) + len(self.mc_labels))
            metadata["mc_labels"] = self.column_names + self.mc_labels
        else:
            shape = (self.chunk_shape, len(self.column_names))
            maxshape = (None, len(self.column_names))
            metadata["mc_labels"] = self.column_names

        if self.write_mc:
            self.create_datasets(
                dataset_names=["mc"] if self.n_piles is None else self.pile_datasets_dct["mc"],
                shape=shape,
                maxshape=maxshape,
                **self.hdf5_kwargs,
            )

        if self.write_data:
            data_column_names = list(set(self.column_names) - set(self.mc_only_column_names))
            metadata["data_labels"] = data_column_names

            self.create_datasets(
                mode="a" if self.write_mc else "w",
                dataset_names=["data"] if self.n_piles is None else self.pile_datasets_dct["data"],
                shape=(self.chunk_shape, len(data_column_names)),
                maxshape=(None, len(data_column_names)),
                **self.hdf5_kwargs,
            )

        if self.n_piles is not None:
            metadata["piles"] = self.pile_datasets_dct

        self.add_metadata(metadata)

        return self

    def run_default(self, processors):
        if self.is_data and not self._current_is_data:
            self._current_is_data = True
            self._current_idx, self._current_shape = 0, self.chunk_shape

        if not self.is_data and self._current_is_data:
            self._current_is_data = False
            self._current_idx, self._current_shape = 0, self.chunk_shape

        arrays = processors[self.save_node].arrays
        report = processors["input"]._reports[0]

        save_arrays = []
        for column_name in self.column_names:
            if column_name not in arrays.fields:
                continue

            column = ak.to_numpy(arrays[column_name])
            column = column[:, None]
            save_arrays.append(column)

        if not self.is_data and self.mc_labels is not None:
            mc_name = report["name"]
            mc_name_idx = self.mc_labels.index(mc_name)

            mc_labels_array = np.zeros((column.shape[0], len(self.mc_labels)))
            mc_labels_array[:, mc_name_idx] = 1.0

            save_arrays.append(mc_labels_array)

        save_arrays = np.concatenate(save_arrays, axis=1)

        array_chunks = len(save_arrays) // self.chunk_shape + 1
        chunk_save_arrays = np.array_split(save_arrays, array_chunks)

        for chunk_array in chunk_save_arrays:
            n_chunk = len(chunk_array)
            start_idx, stop_idx = self._current_idx, self._current_idx + n_chunk

            self._current_idx = stop_idx

            if self._current_idx > self._current_shape:
                resize = (stop_idx, chunk_array.shape[1])
                self._current_shape = stop_idx
            else:
                resize = None

            self.add_data(chunk_array, "mc" if not self.is_data else "data", idx=(start_idx, stop_idx), resize=resize)

        return {"processors": processors}

    def run_piles(self, processors):
        pile_idx = np.random.choice(self.n_piles)

        if self.is_data:
            dataset_name = "data"
        else:
            dataset_name = "mc"

        pile_name = self.pile_datasets_dct[dataset_name][pile_idx]

        arrays = processors[self.save_node].arrays
        report = processors["input"]._reports[0]

        save_arrays = []
        for column_name in self.column_names:
            if column_name not in arrays.fields:
                continue

            column = ak.to_numpy(arrays[column_name])
            column = column[:, None]
            save_arrays.append(column)

        if not self.is_data and self.mc_labels is not None:
            mc_name = report["name"]
            mc_name_idx = self.mc_labels.index(mc_name)

            mc_labels_array = np.zeros((column.shape[0], len(self.mc_labels)))
            mc_labels_array[:, mc_name_idx] = 1.0

            save_arrays.append(mc_labels_array)

        save_arrays = np.concatenate(save_arrays, axis=1)

        array_chunks = len(save_arrays) // self.chunk_shape + 1
        chunk_save_arrays = np.array_split(save_arrays, array_chunks)

        for chunk_array in chunk_save_arrays:
            n_chunk = len(chunk_array)
            start_idx = self.piles_info_dct[dataset_name][pile_name]["current_idx"]
            stop_idx = self.piles_info_dct[dataset_name][pile_name]["current_idx"] + n_chunk

            self.piles_info_dct[dataset_name][pile_name]["current_idx"] = stop_idx

            if (
                self.piles_info_dct[dataset_name][pile_name]["current_idx"]
                > self.piles_info_dct[dataset_name][pile_name]["current_shape"]
            ):
                resize = (stop_idx, chunk_array.shape[1])
                self.piles_info_dct[dataset_name][pile_name]["current_shape"] = stop_idx
            else:
                resize = None

            self.add_data(chunk_array, pile_name, idx=(start_idx, stop_idx), resize=resize)

        return {"processors": processors}

    def run(self, processors):
        if self.n_piles is None:
            return self.run_default(processors)
        else:
            return self.run_piles(processors)
