import argparse
import os
import re
import time

import pandas as pd

from f9columnar.submit.act_submit import ActBatchSubmitter


class ActBatchGetter:
    def __init__(self, jobs_dir, retry_empty=True, direct_retry=False, include_finishing=False):
        """Act `get` wrapper for batch jobs.

        Parameters
        ----------
        jobs_dir : str
            Directory containing .xrsl files.
        retry_empty : bool, optional
            If True will retry empty jobs, by default True.
        direct_retry : bool, optional
            If False will try to download jobs few times before resubmitting empty jobs, by default False.
        include_finishing : bool, optional
            If True will include jobs in finishing state, by default False.

        Note
        ----
        If retry_empty is False, will just download the jobs.
        If retry_empty is True and direct_retry is False, will try to download jobs few times before resubmitting empty jobs.
        If retry_empty is True and direct_retry is True, will download jobs and submit empty jobs again directly.
        If include_finishing is True and retry_empty is True then direct_retry must be set to False.

        """
        self.jobs_dir = jobs_dir
        self.retry_empty = retry_empty
        self.direct_retry = direct_retry
        self.include_finishing = include_finishing

        if include_finishing and retry_empty and direct_retry:
            print("Switching to direct_retry=False.")
            self.direct_retry = False

        self.submitter = ActBatchSubmitter(jobs_dir, retry_empty=retry_empty)

    def _get(self, clean=False):
        if clean:
            os.system("act get -a --use-jobname")
        else:
            os.system("act get -a --noclean --use-jobname")

        if self.include_finishing:
            self._get_finishing(clean)

        dirs = [f.path[2:] for f in os.scandir(".") if f.is_dir()]

        output_dirs = []
        for d in dirs:
            if "mc" in d or "data" in d:
                output_dirs.append(d)

        print(f"Found {len(output_dirs)} output directories.")

        if len(output_dirs) == 0:
            print("No output directories found!")

        os.makedirs(f"{self.jobs_dir}/out", exist_ok=True)
        for d in output_dirs:
            os.system(f"mv {d} {self.jobs_dir}/out/{d}")

        if len(output_dirs) != 0:
            print(f"Moved output directories to {self.jobs_dir}/out.")

        return output_dirs

    def _get_finishing(self, clean=False):
        os.system("act stat -a > act_stat_finishing.txt")
        df = pd.read_csv("act_stat_finishing.txt", delimiter=r"\s+")

        os.system("rm -f act_stat_finishing.txt")

        finishing_df = df[(df["State"] == "Finishing") & (df["arcstate"] == "finishing")]
        finshing_id, finishing_job_name = finishing_df["id"].values, finishing_df["jobname"].values

        for job_id, job_name in zip(finshing_id, finishing_job_name):
            print(f"Getting finishing job {job_name}.")
            if clean:
                os.system(f"act get -i {job_id} --use-jobname")
            else:
                os.system(f"act get -i {job_id} --noclean --use-jobname")

    def _get_done(self):
        os.system("act stat -a > act_stat_done.txt")
        df = pd.read_csv("act_stat_done.txt", delimiter=r"\s+")

        os.system("rm -f act_stat_done.txt")

        if self.include_finishing:
            done_df = df[
                ((df["State"] == "Finished") & (df["arcstate"] == "done"))
                | ((df["State"] == "Finishing") & (df["arcstate"] == "finishing"))
            ]
        else:
            done_df = df[(df["State"] == "Finished") & (df["arcstate"] == "done")]

        done_id, done_job_name = done_df["id"].values, done_df["jobname"].values

        empty_jobs_xrsl, empty_dirs = self.submitter._get_empty_jobs(return_dirs=True)
        empty_jobs = [os.path.basename(j)[:-5] for j in empty_jobs_xrsl]

        for job_id, job_name in zip(done_id, done_job_name):
            if job_name in empty_jobs:
                print(f"Job {job_name} results are empty.")

                empty_dir_idx = empty_jobs.index(job_name)
                print(f"Removing {empty_dirs[empty_dir_idx]}.")
                os.system(f"rm -rf {empty_dirs[empty_dir_idx]}")
            else:
                print(f"Cleaning job {job_name}.")
                os.system(f"act clean -i {job_id} >/dev/null 2>&1")

        return empty_jobs

    def get(self, max_retries=3, timeout=5):
        if not self.retry_empty:
            self._get(clean=True)
            return self

        elif self.direct_retry and self.retry_empty:
            self._get(clean=True)
            self.submitter.submit()
            return self

        elif not self.direct_retry and self.retry_empty:
            for _ in range(max_retries):
                output_dirs = self._get()
                if len(output_dirs) == 0:
                    print("All jobs downloaded successfully!")
                    return self

                empty_jobs = self._get_done()

                if len(empty_jobs) == 0:
                    print("All jobs downloaded successfully!")
                    return self
                else:
                    print("Retrying...")
                    time.sleep(timeout)

            print(50 * "=")
            print("Max retries reached, will submit empty jobs again.")
            print(f"Submitting empty jobs to ActBatchSubmitter: {empty_jobs}")
            print(50 * "=")

            self._get(clean=True)
            self.submitter.submit()

            return self

        else:
            raise ValueError("Invalid combination of retry_empty and direct_retry.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch getter.")

    parser.add_argument(
        "--jobs_dir",
        type=str,
        help="Directory containing .xrsl files.",
        default="batch/run_0",
    )
    parser.add_argument(
        "--retry_empty",
        type=lambda x: str(x).lower() == "true",
        help="Retry empty jobs.",
        default=True,
    )
    parser.add_argument(
        "--direct_retry",
        type=lambda x: (str(x).lower() == "true"),
        help="If False will try to download jobs few times before resubmitting empty jobs.",
        default=True,
    )
    parser.add_argument(
        "--include_finishing",
        type=lambda x: (str(x).lower() == "true"),
        help="If True will include jobs in finishing state.",
        default=False,
    )
    args = parser.parse_args()

    act_getter = ActBatchGetter(args.jobs_dir, args.retry_empty, args.direct_retry, args.include_finishing)
    act_getter.get()
