import gc
import logging
import os

import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
from tqdm import tqdm

from f9columnar.object_collections import Cut
from f9columnar.plotting import set_default_font_family
from f9columnar.utils.helpers import dump_json, get_ms_datetime
from f9columnar.utils.loggers import timeit


class CutFlow:
    def __init__(self):
        """Logging class for cut flow of processors."""
        self.cut_flow = {"mc": {}, "data": {}}

        self.save_dir = f"logs/cut_flow/{get_ms_datetime()}"
        os.makedirs(self.save_dir, exist_ok=True)

    @staticmethod
    def _get_n(cut_processors):
        processors_cut_dct = {}

        for processor_name, processor in cut_processors.items():
            if isinstance(processor, Cut):
                start_n, end_n = processor.start_n, processor.end_n
                processors_cut_dct[processor_name] = [start_n, end_n]

        return processors_cut_dct

    def _add_to_cut_flow(self, name, dct_key, n_dct):
        if name not in self.cut_flow[dct_key]:
            n_counts = {}
            for processor_name in n_dct.keys():
                n_counts[processor_name] = []

            self.cut_flow[dct_key][name] = n_counts

        for processor_name, cut_values_lst in n_dct.items():
            self.cut_flow[dct_key][name][processor_name].append(cut_values_lst)

        return self

    def add(self, cut_processors, is_data=False):
        n_dct = self._get_n(cut_processors)

        if is_data:
            self._add_to_cut_flow("Data", "data", n_dct)
        else:
            self._add_to_cut_flow("MC", "mc", n_dct)

        return self

    def plot(self, is_data=False, n_start=False):
        set_default_font_family()

        if is_data:
            flow_dct, postfix = self.cut_flow["data"], "data"
        else:
            flow_dct, postfix = self.cut_flow["mc"], "mc"

        dump_json(flow_dct, f"{self.save_dir}/cut_flow_{postfix}.json")

        for name, processor_dct in flow_dct.items():
            processor_names = list(processor_dct.keys())

            if len(processor_names) == 0:
                logging.warning("No processors in cut flow!")
                return None

            x_values, y_values = [], []
            for i, cut_values in enumerate(processor_dct.values()):
                cut_values = np.array(cut_values)

                x_values.append(i)

                if n_start:
                    y_values.append(np.sum(cut_values[:, 0]))
                else:
                    y_values.append(np.sum(cut_values[:, 1]))

            fig, ax = plt.subplots(figsize=(len(processor_names) * 0.5, 8))
            hep.atlas.label(loc=0, llabel="Work in Progress", rlabel="", ax=ax, fontname="Latin Modern sans")

            ax.bar(x_values, y_values)
            ax.set_xticks(x_values)
            ax.set_xticklabels(processor_names, rotation=90)
            ax.set_ylabel(f"Cut flow for {name}")
            ax.set_yscale("log")

            fig.tight_layout()

            i = 0
            while os.path.exists(f"{self.save_dir}/{name}_{i}.pdf"):
                i += 1

            fig.savefig(f"{self.save_dir}/{name}_{i}.pdf")
            plt.close(fig)


class TimeFlow(CutFlow):
    def __init__(self):
        super().__init__()
        """Logging class for time execution (flow) of processors."""

        self.save_dir = f"logs/time_flow/{get_ms_datetime()}"
        os.makedirs(self.save_dir, exist_ok=True)

    @staticmethod
    def _get_n(cut_processors):
        processors_cut_dct = {}

        for processor_name, processor in cut_processors.items():
            delta_time = processor.delta_time
            processors_cut_dct[processor_name] = delta_time

        return processors_cut_dct

    def plot(self, is_data=False):
        set_default_font_family()

        if is_data:
            flow_dct, postfix = self.cut_flow["data"], "data"
        else:
            flow_dct, postfix = self.cut_flow["mc"], "mc"

        dump_json(flow_dct, f"{self.save_dir}/time_flow_{postfix}.json")

        for name, processor_dct in flow_dct.items():
            processor_names = list(processor_dct.keys())

            if len(processor_names) == 0:
                logging.warning("No processors in time flow!")
                return None

            x_values, y_values = [], []
            for i, time_values in enumerate(processor_dct.values()):
                time_values = np.array(time_values)

                x_values.append(i)
                y_values.append(np.sum(time_values))

            fig, ax = plt.subplots(figsize=(len(processor_names) * 0.5, 8))
            hep.atlas.label(loc=0, llabel="Work in Progress", rlabel="", ax=ax, fontname="Latin Modern sans")

            sort_idx = np.argsort(y_values)[::-1]
            y_values = np.array(y_values)[sort_idx]
            processor_names = np.array(processor_names)[sort_idx]

            ax.bar(x_values, 1000 * y_values)
            ax.set_xticks(x_values)
            ax.set_xticklabels(processor_names, rotation=90)
            ax.set_ylabel(f"Time flow for {name} [ms/cpu]")
            ax.set_yscale("log")

            fig.tight_layout()

            i = 0
            while os.path.exists(f"{self.save_dir}/{name}_{i}.pdf"):
                i += 1

            fig.savefig(f"{self.save_dir}/{name}_{i}.pdf")
            plt.close(fig)


class EventTensorLoop:
    def __init__(
        self,
        mc_datasets=None,
        data_datasets=None,
        postprocessors_graph=None,
        fit_postprocessors=True,
        cut_flow=False,
    ):
        """Loop over MC and data datasets using root_dataloader and run postprocessors.

        Parameters
        ----------
        mc_datasets : list or None, optional
            List of MCDataset objects, by default None.
        data_datasets : list or None, optional
            List of DataDataset objects, by default None.
        postprocessors_graph : object or None, optional
            PostprocessorsGraph instance, by default None.
        fit_postprocessors : bool, optional
            Flag to fit postprocessors, by default True.
        cut_flow : bool, optional
            Flag to enable cut (and time) flow. This is for logging only, by default False.
        """
        self.mc_datasets = mc_datasets
        self.data_datasets = data_datasets
        self.postprocessors_graph = postprocessors_graph
        self.fit_postprocessors = fit_postprocessors

        if cut_flow:
            logging.info("[yellow]Cut flow enabled![/yellow]")
            self.cut_flow, self.time_flow = CutFlow(), TimeFlow()
        else:
            self.cut_flow = None

    @property
    def postprocessors(self):
        return self.postprocessors_graph.processors

    def _fit_postprocessors(self, fitted_processors, is_data):
        if self.postprocessors_graph is None:
            return None

        if type(fitted_processors) is not list:
            fitted_processors = [fitted_processors]

        for processors in fitted_processors:
            self.postprocessors_graph.fit(processors, is_data=is_data)

        return self

    def _iterate_dataloaders(self, datasets, is_data):
        desc_ds = "Iterating over data datasets" if is_data else "Iterating over MC datasets"
        desc_dl = "Iterating over data dataloader" if is_data else "Iterating over MC dataloader"

        total = 0
        for dataset in tqdm(datasets, total=len(datasets), desc=desc_ds, leave=True):
            dataloader, num_entries = dataset.dataloader, dataset.num_entries

            bar = tqdm(total=num_entries, desc=f"{desc_dl} for {dataset.name}", leave=False)

            if dataloader is not None:
                for fitted_processors in dataloader:
                    if self.fit_postprocessors:
                        self._fit_postprocessors(fitted_processors, is_data)

                    if "input" in fitted_processors:
                        n_events = fitted_processors["input"].n_events
                        bar.update(n_events)
                        total += n_events

                    if self.cut_flow:
                        self.cut_flow.add(fitted_processors, is_data)
                        self.time_flow.add(fitted_processors, is_data)

                    if self.fit_postprocessors:
                        for k in fitted_processors.keys():
                            fitted_processors[k] = None
            else:
                logging.warning(f"[yellow]No dataloader found for {dataset.name}![/yellow]")

            gc.collect()

        bar.close()
        logging.info(f"Total number of events processed: {total}")

        if self.cut_flow:
            self.cut_flow.plot(is_data)
            self.time_flow.plot(is_data)

        return self

    @timeit(unit="s")
    def run(self, mc_only=False, data_only=False):
        assert not (mc_only and data_only), "Cannot run both MC and data only!"

        if not self.fit_postprocessors:
            logging.info("[yellow]Not fitting postprocessors! Will return fitted processors for MC and data.[/yellow]")

        logging.info("[red][bold]Running event tensor loop![/bold][red]")

        results = {"mc": None, "data": None}

        if mc_only:
            results["mc"] = self._iterate_dataloaders(self.mc_datasets, is_data=False)
        elif data_only:
            results["data"] = self._iterate_dataloaders(self.data_datasets, is_data=True)
        else:
            results["mc"] = self._iterate_dataloaders(self.mc_datasets, is_data=False)
            results["data"] = self._iterate_dataloaders(self.data_datasets, is_data=True)

        logging.info("[red][bold]Done running event tensor loop![/bold][red]")

        if self.fit_postprocessors:
            for postprocessor in self.postprocessors_graph.processors.values():
                postprocessor.save()
            return self
        else:
            return results
