import logging
import pickle
from abc import abstractmethod
from dataclasses import dataclass
from typing import List

import awkward as ak
import hist
import numpy as np

from f9columnar.processors import Postprocessor, Processor
from f9columnar.utils.helpers import dump_pickle


@dataclass
class Hist1d:
    """Dataclass for a 1D histogram. Wraps the hist.Hist object.

    Parameters
    ----------
    name : str
        Name of the histogram.
    nbins : int, optional
        Number of bins, by default None.
    lower : float, optional
        Lower edge of the histogram, by default None.
    upper : float, optional
        Upper edge of the histogram, by default None.
    bins : list | np.ndarray, optional
        Custom bin edges, by default None.
    storage : str, optional
        Storage type, by default "double". Options: "double", "weight". Used for weights and uncertainties. See [1].
    underflow : bool, optional
        Include underflow bin, by default False.
    overflow : bool, optional
        Include overflow bin, by default False.
    log : bool, optional
        Logarithmic binning, by default False. If True, nbins, lower, and upper are needed.
    hist : hist.Hist
        Histogram object. Assigned in post init.

    Note
    ----
    - If bins is provided, nbins, lower, and upper are ignored.
    - If bins is not provided, nbins, lower, and upper are required.

    References
    ----------
    [1] - https://hist.readthedocs.io/en/latest/user-guide/storages.html

    """

    name: str
    nbins: int | None = None
    lower: float | None = None
    upper: float | None = None
    bins: list | np.ndarray | None = None
    storage: str = "double"
    underflow: bool = False
    overflow: bool = False
    log: bool = False
    hist = None

    def _get_regular_binning(self):
        if self.log:
            bins = np.logspace(np.log(self.lower), np.log(self.upper), self.nbins, base=np.e)
            binning = hist.axis.Variable(
                bins,
                name=self.name,
                underflow=self.underflow,
                overflow=self.overflow,
            )
        else:
            binning = hist.axis.Regular(
                self.nbins,
                self.lower,
                self.upper,
                name=self.name,
                underflow=self.underflow,
                overflow=self.overflow,
            )

        return binning

    def _get_variable_binning(self):
        binning = hist.axis.Variable(
            self.bins,
            name=self.name,
            underflow=self.underflow,
            overflow=self.overflow,
        )
        return binning

    def _get_storage(self):
        if self.storage.lower() == "double":
            return hist.storage.Double()
        elif self.storage.lower() == "weight":
            return hist.storage.Weight()
        else:
            raise NotImplementedError(f"Storage type {self.storage} not implemented.")

    def _get_hist(self):
        storage = self._get_storage()

        if self.bins is not None:
            assert self.nbins is None and self.lower is None and self.upper is None
            binning = self._get_variable_binning()
        elif self.nbins is not None and self.lower is not None and self.upper is not None:
            binning = self._get_regular_binning()
        else:
            raise ValueError("Please provide either nbins, lower, and upper or bins.")

        return hist.Hist(binning, name=self.name, storage=storage)

    def __post_init__(self):
        self.hist = self._get_hist()


@dataclass
class HistNd:
    """Dataclass for an N-dimensional histogram. Wraps the hist.Hist object.

    Parameters
    ----------
    name : str
        Name of the histogram.
    hists1d : List[Hist1d]
        List of 1D histograms to build the N-dimensional histogram.
    hist : hist.Hist
        Histogram object. Assigned in post init.
    """

    name: str
    hists1d: List[Hist1d]
    hist = None

    def _get_hist(self):
        axes, storage = [], []
        for hist1d in self.hists1d:
            axes.append(hist1d.hist.axes[hist1d.name])
            storage.append(hist1d.storage)

        storage = list(set(storage))
        assert len(storage) == 1
        storage = storage[0]

        if storage.lower() == "double":
            storage = hist.storage.Double()
        elif storage.lower() == "weight":
            storage = hist.storage.Weight()
        else:
            raise NotImplementedError(f"Storage type {self.storage} not implemented.")

        return hist.Hist(*axes, name=self.name, storage=storage)

    def __post_init__(self):
        self.hist = self._get_hist()


class HistogramProcessor(Processor):
    def __init__(self, name, as_data=None, weights_field=None, auto_fill=True):
        """Histogram processor for making and filling histograms.

        Parameters
        ----------
        name : str
            Name of the processor.
        as_data : bool, optional
            Data flag, by default None.
        weights_field : str, optional
            Weights array field name (e.g. "weight_mc_total"), by default None.
        auto_fill : bool, optional
            Auto fill histograms assuming array field names match histogram names, by default True.

        References
        ----------
        [1] - https://hist.readthedocs.io/en/latest/user-guide/quickstart.html
        [2] - https://mplhep.readthedocs.io/en/latest/api.html
        [3] - https://hsf-training.github.io/analysis-essentials/advanced-python/40Histograms.html

        """
        super().__init__(name)
        self.as_data = as_data
        self.weights_field = weights_field
        self.auto_fill = auto_fill

        self.hists, self.hists_metadata = {}, {}

    def _get_storage_type(self):
        if self.as_data is not None:
            storage_type = "weight"  # need to add unity weights for data!
        else:
            storage_type = "double"

        return storage_type

    def make_hist1d(
        self,
        hist_name,
        nbins=None,
        lower=None,
        upper=None,
        bins=None,
        underflow=False,
        overflow=False,
        log=False,
        hist_kwargs_dct=None,
        storage_type=None,
        return_hist1d=False,
    ):
        """Make a 1D histogram object and store it in the hists dictionary.

        Parameters
        ----------
        hist_name : str
            Name of the 1D histogram.
        hist_kwargs_dct : dict, optional
            Dictionary for building the 1D histogram, by default None.
        storage_type : str, optional
            Storage type, by default None. Options: "double", "weight" or None.
        return_hist1d : bool, optional
            Return the Hist1d dataclass object, by default False.

        Note
        ----
        If hist_kwargs_dct is provided, the other histogram parameters are ignored. If storage_type is None, it is
        determined by the as_data flag. If as_data is True or False, the storage type is "weight". If as_data is None,
        the storage type is "double".

        Warning
        -------
        Unity weights are automatically added for data histograms.

        """
        if storage_type is None:
            storage_type = self._get_storage_type()

        if hist_kwargs_dct is not None:
            hist1d = Hist1d(hist_name, storage=storage_type, **hist_kwargs_dct)
        else:
            hist1d = Hist1d(hist_name, nbins, lower, upper, bins, storage_type, underflow, overflow, log)

        if return_hist1d:
            return hist1d

        self.hists[hist_name] = hist1d.hist

        return self

    def make_histNd(self, hist_name, hist1d_kwargs_dcts, storage_type=None):
        """Make an N-dimensional histogram object and store it in the hists dictionary.

        Parameters
        ----------
        hist_name : str
            Name of the N-dimensional histogram.
        hist1d_kwargs_dcts : dict
            Dictionary of 1D histogram kwargs for building the N-dimensional histogram.
        storage_type : str, optional
            Storage type, by default None. Options: "double", "weight" or None.

        """
        if storage_type is None:
            storage_type = self._get_storage_type()

        hists1d = []
        for hist1d_name, hist_kwargs_dct in hist1d_kwargs_dcts.items():
            hist1d = self.make_hist1d(
                hist1d_name,
                storage_type=storage_type,
                hist_kwargs_dct=hist_kwargs_dct,
                return_hist1d=True,
            )
            hists1d.append(hist1d)

        histNd = HistNd(hist_name, hists1d)
        self.hists[hist_name] = histNd.hist

        return self

    def fill_hist1d(self, hist_name, data, weight=None, metadata=None):
        """Fill a 1D histogram with data and weight. Optionally store metadata."""
        self.hists[hist_name].fill(data, weight=weight)
        self.hists_metadata[hist_name] = metadata
        return self

    def fill_histNd(self, hist_name, data_lst, weight=None, metadata=None):
        """Fill an N-dimensional histogram with data and weight. Optionally store metadata."""
        self.hists[hist_name].fill(*data_lst, weight=weight)
        self.hists_metadata[hist_name] = metadata
        return self

    def get_hist(self, hist_name):
        return self.hists[hist_name]

    def get_hist_names(self):
        return list(self.hists.keys())

    def get_hist_info(self, hist_name):
        return {
            "egdes": self.hists[hist_name].axes[hist_name].edges,
            "centers": self.hists[hist_name].axes[hist_name].centers,
            "widths": self.hists[hist_name].axes[hist_name].widths,
        }

    def get_hist_values(self, hist_name):
        return {
            "values": self.hists[hist_name].values(),
            "variances": self.hists[hist_name].variances(),
        }

    def __getitem__(self, hist_name):
        return self.get_hist(hist_name)

    def auto_fill_hist(self, arrays, weight):
        for hist_name in self.hists.keys():
            if hist_name in arrays.fields:
                self.fill_hist1d(hist_name, arrays[hist_name], weight=weight, metadata=self.reports)
        return None

    def init_run(self, arrays):
        """Initializes the run method by checking if the processor should run. If not, returns True and None.

        Note
        ----
        If the as_data flag is different from the is_data flag, the processor will not run. This is useful for
        separating MC and data histograms.

        Warning
        -------
        This method should be called at the beginning of the run method in the derived class to correctly check if the
        processor should run and assign the weight array.

        """
        if self.as_data != self.is_data:
            pass_run = True
        else:
            pass_run = False

        if pass_run:
            return pass_run, None

        if not self.is_data:
            if self.weights_field is not None:
                weight = arrays[self.weights_field]
            else:
                weight = None
        else:
            weight = ak.Array(np.ones(len(arrays), dtype=np.float32))

        return pass_run, weight

    @abstractmethod
    def run(self, arrays):
        pass_run, weight = self.init_run(arrays)

        if pass_run:
            return {"arrays": arrays}

        if self.auto_fill:
            self.auto_fill_hist(arrays, weight)

        return {"arrays": arrays}


class HistogramMerger(Postprocessor):
    def __init__(self, name, save_path=None, mc_hist_name=None, data_hist_name=None):
        super().__init__(name)
        self.save_path = save_path
        self.mc_hist_name = mc_hist_name
        self.data_hist_name = data_hist_name

        self.merged_hists = {}

    def _merge_hists(self, hists_processor):
        hists = hists_processor.hists

        if self.is_data and "data" not in self.merged_hists:
            self.merged_hists["data"] = hists
            return self

        if not self.is_data and "mc" not in self.merged_hists:
            self.merged_hists["mc"] = hists
            return self

        for hist_name, hist_obj in hists.items():
            if self.is_data:
                self.merged_hists["data"][hist_name] += hist_obj
            else:
                self.merged_hists["mc"][hist_name] += hist_obj

        return self

    def run(self, processors):
        if self.is_data:
            if self.data_hist_name:
                hists_processor = processors[self.data_hist_name]
                self._merge_hists(hists_processor)
        else:
            if self.mc_hist_name:
                hists_processor = processors[self.mc_hist_name]
                self._merge_hists(hists_processor)

        return {"processors": processors}

    def save(self):
        assert ".p" in self.save_path, "Please provide a .p file extension for saving histograms."

        dump_pickle(self.save_path, self.merged_hists)

        logging.info(f"[green]Saved merged histograms to {self.save_path}![/green]")
        return self


class NtupleHistogramMerger(Postprocessor):
    def __init__(
        self,
        name="histogram_merger",
        save_path=None,
        mc_hist_name=None,
        data_hist_name=None,
        merge_years=True,
        merge_campaigns=True,
    ):
        super().__init__(name, save_path)
        assert ".p" in self.save_path, "Please provide a .p file extension for saving histograms."

        self.mc_hist_name, self.data_hist_name = mc_hist_name, data_hist_name
        self.merge_years, self.merge_campaigns = merge_years, merge_campaigns

        self.merged_hists = {}

    def _get_name_hists_dct(self, hists, hists_metadata):
        name_hists_dct = {}

        for hist_name, hist_obj in hists.items():

            dataset_names = []
            for metadata_dct in hists_metadata[hist_name]:
                dataset_names.append(metadata_dct["name"])

            assert len(set(dataset_names)) == 1
            dataset_name = dataset_names[0]

            if self.is_data and self.merge_years:
                dataset_name = "_".join(dataset_name.split("_")[:-1])

            if not self.is_data and self.merge_campaigns:
                dataset_name = "_".join(dataset_name.split("_")[:-1])

            if dataset_name not in name_hists_dct:
                name_hists_dct[dataset_name] = {}

            name_hists_dct[dataset_name][hist_name] = hist_obj

        return name_hists_dct

    def _merge(self, name_hists_dct):
        for name, hists_dct in name_hists_dct.items():
            if name not in self.merged_hists:
                self.merged_hists[name] = hists_dct
            else:
                for hist_name, hist_obj in hists_dct.items():
                    self.merged_hists[name][hist_name] += hist_obj

        return self.merged_hists

    def run(self, processors):
        if self.is_data:
            if self.data_hist_name:
                hists_processor = processors[self.data_hist_name]
        else:
            if self.mc_hist_name:
                hists_processor = processors[self.mc_hist_name]

        hists = hists_processor.hists
        hists_metadata = hists_processor.hists_metadata

        name_hists_dct = self._get_name_hists_dct(hists, hists_metadata)
        self._merge(name_hists_dct)

        return {"processors": processors}

    def save(self):
        dump_pickle(self.save_path, self.merged_hists)

        logging.info(f"[green]Saved merged histograms to {self.save_path}![/green]")
        return self


def merge_batch_histograms(merged_pickle, output_key, return_data=True):
    """Merge output histograms from act_merge.

    Parameters
    ----------
    merged_pickle : str
        Path to the merged pickle file.
    output_key : str
        Key of the output histograms (i.e. "el_histograms").
    return_data : bool, optional
        If True pop data key from merged and return it, by default True.

    Returns
    -------
    dict or (dict, dict)
        Merged (summed) histograms for each variable in each histogram name.
    """

    with open(merged_pickle, "rb") as f:
        merged = pickle.load(f)

    outputs = merged["outputs"]
    hists = outputs[output_key]

    merge_hist_dct = {}
    for hs in hists:
        for hist_name, hist_dct in hs.items():
            if len(hist_dct) == 0:
                continue

            if hist_name not in merge_hist_dct:
                merge_hist_dct[hist_name] = {}

            for var_name, var_hist in hist_dct.items():
                if var_name not in merge_hist_dct[hist_name]:
                    merge_hist_dct[hist_name][var_name] = []

                merge_hist_dct[hist_name][var_name].append(var_hist)

    for hist_name, var_dct in merge_hist_dct.items():
        for var_name, var_hist_lst in var_dct.items():
            merge_hist_dct[hist_name][var_name] = sum(var_hist_lst)

    if return_data:
        data = merge_hist_dct.pop("data")
        return merge_hist_dct, data
    else:
        return merge_hist_dct
