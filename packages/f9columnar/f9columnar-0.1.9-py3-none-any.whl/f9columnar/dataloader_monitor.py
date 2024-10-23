import csv
import datetime
import glob
import logging
import os
import re

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mplhep as hep
import pandas as pd
import seaborn as sns

from f9columnar.plotting import set_size
from f9columnar.utils.helpers import get_ms_time


class WorkerHeartbeat:
    def __init__(self, worker_id, run_name="worker_logs", prefix="", fields=None):
        self.worker_id = worker_id
        self.run_name = run_name

        self.csv_file, self.csv_writer = None, None
        self.start_time = self.get_current_time()

        self.dir_name = f"logs/{self.run_name}/heartbeat"

        os.makedirs(self.dir_name, exist_ok=True)

        self.file_name = f"{self.dir_name}/{prefix}_{self.worker_id}.csv"

        self.fields = ["worker_id", "current_time", "elapsed_time"]
        if fields is not None:
            self.fields += fields

    def open(self, mode="a+"):
        self.csv_file = open(self.file_name, mode)
        self.csv_writer = csv.writer(self.csv_file, delimiter=",")
        return self

    def close(self):
        self.csv_file.close()
        self.csv_file, self.csv_writer = None, None
        return self

    def _write_to_csv(self, data_lst):
        self.csv_writer.writerow(data_lst)
        self.csv_file.flush()
        return self

    def get_current_time(self):
        return get_ms_time()

    def write_heartbeat(self, data_lst):
        write_time = self.get_current_time()
        data_lst = [self.worker_id, write_time, write_time - self.start_time] + data_lst
        self._write_to_csv(data_lst)
        return self


class WorkerLogger:
    def __init__(self, num_workers, run_name="worker_logs", log_name="root_workers"):
        self.num_workers = num_workers
        self.run_name = run_name
        self.log_name = log_name

        self.dir_name = f"logs/{self.run_name}/{self.log_name}"

        os.makedirs(self.dir_name, exist_ok=True)
        for f in glob.glob(f"{self.dir_name}/*"):
            try:
                os.remove(f)
            except Exception as e:
                logging.info(f"Error removing file {f}: {e}")

    @staticmethod
    def _ms_stamp_to_datetime(stamp):
        return datetime.datetime.fromtimestamp(int(stamp) // 1000)

    def _get_worker_logs(self, stamp):
        stamp = self._ms_stamp_to_datetime(stamp)
        glob_res = glob.glob(f"{self.dir_name}/*_{stamp}.csv")
        return list(set([f for f in glob_res if re.search(rf"{self.dir_name}/\d+", f)]))

    def _log_worker(self, worker_dct, worker_id, stamp):
        log_dct = {
            "file": [],
            "n_start": [],
            "n_stop": [],
            "n_total": [],
            "n_iterations": [],
            "n_entries_for": [],
        }

        for iterator in worker_dct.values():
            log_dct["file"].append("/".join(iterator.root_file.split("/")[-2:]))
            log_dct["n_start"].append(iterator.entry_start)
            log_dct["n_stop"].append(iterator.entry_stop)
            log_dct["n_total"].append(iterator.num_entries)
            log_dct["n_iterations"].append(iterator.num_iterations)
            log_dct["n_entries_for"].append(iterator.num_entries_for)

        df = pd.DataFrame(log_dct)
        df["worker_id"] = worker_id

        stamp = self._ms_stamp_to_datetime(stamp)
        df.to_csv(f"{self.dir_name}/{worker_id}_{stamp}.csv", index=False)

        return self

    def _parse_worker_logs(self, stamp):
        worker_logs = self._get_worker_logs(stamp)

        dfs = []
        for log in worker_logs:
            dfs.append(pd.read_csv(log))

        worker_df = pd.concat(dfs)

        worker_df.sort_values(by=["file", "n_start"], inplace=True)
        worker_df.reset_index(drop=True, inplace=True)

        worker_load_df = worker_df.groupby("worker_id").agg({"n_total": "sum", "n_iterations": "sum"})
        worker_load_df["n_per_iter"] = worker_load_df["n_total"] / worker_load_df["n_iterations"]
        worker_load_df["n_mean"] = worker_df.groupby(["worker_id"])["n_total"].mean()
        worker_load_df.sort_values(by=["n_total"], ascending=False, inplace=True)

        file_load_df = worker_df.groupby("file").agg({"n_total": "sum", "n_iterations": "sum"})
        file_load_df["n_per_iter"] = file_load_df["n_total"] / file_load_df["n_iterations"]
        file_load_df.sort_values(by=["n_total"], ascending=False, inplace=True)

        stamp = self._ms_stamp_to_datetime(stamp)

        worker_df.to_csv(f"{self.dir_name}/info_{stamp}.csv", index=False)
        worker_load_df.to_csv(f"{self.dir_name}/load_{stamp}.csv", index=True)
        file_load_df.to_csv(f"{self.dir_name}/file_load_{stamp}.csv", index=True)

        return self

    def __call__(self, worker_dct, worker_id, stamp):
        try:
            self._log_worker(worker_dct, worker_id, str(stamp))

            worker_logs = self._get_worker_logs(stamp)

            if len(worker_logs) == self.num_workers:
                self._parse_worker_logs(stamp)

        except Exception as e:
            logging.debug(f"Error logging worker information: {e}")

        return self


class LiveMonitor:
    def __init__(self, figsize=(12, 6), run_name="worker_logs"):
        self.dir_name = f"logs/{run_name}/heartbeat"
        assert os.path.exists(self.dir_name), f"Directory {self.dir_name} does not exist!"

        self.heartbeat_files, self.data_dct, self.colors, self.start_time = None, {}, None, None
        self._setup()

        self.fig, self.axs = plt.subplots(1, 2, figsize=figsize, dpi=1920 / 16)
        self.axs.flatten()

        self._set_labels()

        self.current_time, self.elapsed_time = [], []

    @staticmethod
    def _setup():
        try:
            import warnings

            import matplotlib

            warnings.filterwarnings("ignore")
            matplotlib.use("Qt5Agg")

            set_size()
            plt.style.use([hep.style.ATLAS])
        except Exception as e:
            logging.info(f"Error setting up plotter failed with: {e}")

    def _set_labels(self):
        for ax in self.axs:
            ax.set_xlabel("Time (s)")

        self.axs[0].set_ylabel("Events")
        self.axs[1].set_ylabel("Total data (MB)")

        hep.atlas.label(loc=4, llabel="Work in Progress", rlabel="", ax=self.axs[0])

    def _get_files(self):
        self.heartbeat_files = glob.glob(f"{self.dir_name}/iterator_*.csv")
        assert len(self.heartbeat_files) > 0, f"No heartbeat files found in {self.dir_name}!"
        return self

    def _get_data_dct(self):
        for worker_id in range(len(self.heartbeat_files)):
            if worker_id not in self.data_dct:
                self.data_dct[worker_id] = {
                    "events": [],
                    "sum_events": [],
                    "size": [],
                    "sum_size": [],
                }
        return self

    def _get_colors(self):
        self.colors = sns.cubehelix_palette(n_colors=len(self.data_dct))
        return self

    def _get_start_time(self):
        df = self._read_csv(self.heartbeat_files[0])
        self.start_time = df["current_time"].values[0] / 1000
        return self

    @staticmethod
    def _read_csv(f):
        return pd.read_csv(f, names=["worker_id", "current_time", "elapsed_time", "iterations", "events", "size"])

    def _plot_setup(self):
        self._get_files()
        self._get_data_dct()
        self._get_colors()
        self._get_start_time()

    def plot(self, frame):
        self._plot_setup()

        self.current_time.append(get_ms_time() / 1000)
        self.elapsed_time.append(self.current_time[-1] - self.start_time)

        for f in self.heartbeat_files:
            df = self._read_csv(f)

            try:
                worker_id = df["worker_id"].values[0]

                self.data_dct[worker_id]["events"].append(df["events"].values[-1])
                self.data_dct[worker_id]["sum_events"].append(sum(df["events"]))
                self.data_dct[worker_id]["size"].append(df["size"].values[-1])
                self.data_dct[worker_id]["sum_size"].append(sum(df["size"]))

            except IndexError:
                continue

        event_stack, data_stack = [], []
        for i in range(len(self.data_dct)):
            event_stack.append(self.data_dct[i]["sum_events"])
            data_stack.append(self.data_dct[i]["sum_size"])

        for i, (ev, data) in enumerate(zip(event_stack, data_stack)):
            # fix if new worker is added
            z_pad = len(self.elapsed_time) - len(ev)
            event_stack[i] = [0] * z_pad + ev
            data_stack[i] = [0] * z_pad + data

        self.axs[0].stackplot(self.elapsed_time, event_stack, colors=self.colors)
        self.axs[1].stackplot(self.elapsed_time, data_stack, colors=self.colors)

        for ax in self.axs:
            ax.set_xlim(self.elapsed_time[0], self.elapsed_time[-1])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ROOT dataloader live matplotlib plotter.")

    parser.add_argument(
        "-n",
        "--run_name",
        default="root_dl",
        type=str,
        help="Logs directory name.",
    )
    parser.add_argument(
        "-fps",
        "--frames",
        default=60,
        type=int,
        help="Frames per second.",
    )
    parser.add_argument(
        "-i",
        "--interval",
        default=100,
        type=int,
        help="Refesh interval in ms.",
    )

    args = parser.parse_args()

    plotter = LiveMonitor(run_name=args.run_name)

    live_plot = animation.FuncAnimation(plotter.fig, plotter.plot, interval=args.interval, frames=args.frames)

    plt.tight_layout()
    plt.show()
