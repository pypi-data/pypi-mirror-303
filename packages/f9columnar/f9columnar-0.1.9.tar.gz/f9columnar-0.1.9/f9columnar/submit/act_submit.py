import argparse
import glob
import os

import pandas as pd
import yaml


class ActBatchSubmitter:
    def __init__(
        self,
        jobs_dir,
        cluster_lst=None,
        retry_failed=False,
        retry_stuck=False,
        retry_empty=False,
        retry_missing=False,
    ):
        """Class for submitting batch jobs to ARC using aCT.

        Parameters
        ----------
        jobs_dir : str
            Directory containing .xrsl files.
        cluster_lst : list, optional
            List of sites to use, by default None. If None will use arc-client/config.yaml.
        retry_failed : bool, optional
            Retry (resubmit xrsl) failed jobs (state and arcstate failed), by default False.
        retry_stuck : bool, optional
            Retry (resubmit xrsl) stuck jobs (state running and arcstate cancelled), by default False.
        retry_empty : bool, optional
            Retry (resubmit xrsl) empty jobs (missing output files), by default False.
        retry_missing : bool, optional
            Retry (resubmit xrsl) missing jobs (missing output files), by default False.

        Note
        ----
        Need to `export PYTHONPATH=.` if running this script from act_venv.

        aCT usage
        ---------
        usage: act [-h] [--server SERVER] [--port PORT] [--conf CONF] [-v]
           {info,clean,fetch,get,kill,proxy,resub,stat,sub,cat} ...

        positional arguments:
        {info,clean,fetch,get,kill,proxy,resub,stat,sub,cat}
            info                show info about aCT server
            clean               clean failed, done and donefailed jobs
            fetch               fetch failed jobs
            get                 download results of done and donefailed jobs
            kill                kill jobs
            proxy               submit proxy certificate
            resub               resubmit failed jobs
            stat                print status for jobs
            sub                 submit job descriptions
            cat                 print stdout or stderr of the job

        optional arguments:
        -h, --help            show this help message and exit
        --server SERVER       URL of aCT server
        --port PORT           port of aCT server
        --conf CONF           path to configuration file
        -v, --verbose         output debug logs

        References
        ----------
        [1] - https://indico.ijs.si/event/2165/#2-act-hands-on-tutorial

        """
        self.jobs_dir = jobs_dir
        self.run_name = jobs_dir.split("/")[-1]

        if cluster_lst is None:
            with open("f9columnar/submit/config/act-client/config.yaml", "r") as f:
                config = yaml.safe_load(f)

            cluster_lst = config["clusters"]["use"]

        self.cluster_lst = ",".join(cluster_lst) if cluster_lst is not None else None

        self.retry_failed = retry_failed
        self.retry_stuck = retry_stuck
        self.retry_empty = retry_empty
        self.retry_missing = retry_missing

    def _get_xrsl_files(self):
        return glob.glob(f"{self.jobs_dir}/*.xrsl")

    def _get_failed_jobs(self):
        os.system("act stat -a > logs/act_stat_retry.txt")
        df = pd.read_csv("logs/act_stat_retry.txt", delimiter=r"\s+")

        os.system("rm -f logs/act_stat_retry.txt")

        failed_jobs = []

        if self.retry_failed:
            failed = df[(df["State"] == "Failed") & (df["arcstate"] == "failed")]
            failed_jobs += list(failed["jobname"].values)

            print("Cleaning failed jobs...")
            job_ids = failed["id"].values
            for job_id in job_ids:
                os.system(f"act clean -i {job_id} >/dev/null 2>&1")

        if self.retry_stuck:
            stuck = df[
                (df["State"] == "Running") & ((df["arcstate"] == "cancelled") | (df["arcstate"] == "cancelling"))
            ]
            failed_jobs += list(stuck["jobname"].values)

        failed_jobs = [f"batch/{self.run_name}/{j}.xrsl" for j in failed_jobs]

        return failed_jobs

    def _get_empty_jobs(self, return_dirs=False):
        out_dir = f"batch/{self.run_name}/out"

        dirs = [f.path for f in os.scandir(out_dir) if f.is_dir()]

        empty_dirs = []
        for d in dirs:
            output_log = f"{d}/log/output"

            with open(output_log, "r") as f:
                log_lines = f.readlines()

                for i, line in enumerate(log_lines):
                    line = line.strip()[1:]
                    if line[-1] == "/":
                        log_lines[i] = line[:-1]
                    else:
                        log_lines[i] = line

                log_lines = list(set(log_lines))

            out_files = os.listdir(d)

            if set(log_lines) != set(out_files):
                empty_dirs.append(d)

        empty_jobs = [os.path.basename(d) for d in empty_dirs]
        empty_jobs = [f"batch/{self.run_name}/{j}.xrsl" for j in empty_jobs]

        if return_dirs:
            return empty_jobs, empty_dirs
        else:
            return empty_jobs

    def _get_missing_jobs(self):
        out_dir = f"batch/{self.run_name}/out"

        dirs = [f.path for f in os.scandir(out_dir) if f.is_dir()]
        present_jobs = set([os.path.basename(d) for d in dirs])

        xrsl_files = self._get_xrsl_files()
        all_jobs = set([os.path.basename(f)[:-5] for f in xrsl_files])

        print(f"Present jobs: {len(present_jobs)}, all jobs: {len(all_jobs)}")
        missing_jobs = list(all_jobs - present_jobs)

        missing_jobs_xrsl_files = []
        for missing_job in missing_jobs:
            missing_jobs_xrsl_files.append(f"{self.jobs_dir}/{missing_job}.xrsl")

        return missing_jobs_xrsl_files

    def _submit(self, n_jobs, jobs):
        if len(jobs) == 0:
            print("No jobs found!")
            return None

        if n_jobs is not None:
            jobs = jobs[:n_jobs]

        for i, job in enumerate(jobs):
            print(30 * "=")
            print(f"Job {i}/{len(jobs)}")

            if self.cluster_lst is None:
                os.system(f"act sub {job}")
            else:
                os.system(f"act sub {job} --clusterlist {self.cluster_lst}")

        return self

    def submit(self, n_jobs=None):
        if any([self.retry_failed, self.retry_stuck, self.retry_empty, self.retry_missing]):
            retry, jobs = True, []
        else:
            retry, jobs = False, self._get_xrsl_files()

        if self.retry_failed or self.retry_stuck:
            print("Retrying failed jobs...")
            try:
                failed_jobs = self._get_failed_jobs()
            except Exception as e:
                print(f"Failed to get failed jobs with exception: {e}")
                failed_jobs = []

            if len(failed_jobs) == 0:
                print("No failed jobs found!")

            jobs += failed_jobs

        if self.retry_empty:
            print("Retrying empty jobs...")
            try:
                empty_jobs, empty_dirs = self._get_empty_jobs(return_dirs=True)
            except Exception as e:
                print(f"Failed to get empty jobs with exception: {e}")
                empty_jobs, empty_dirs = [], []

            if len(empty_jobs) == 0:
                print("No empty jobs found!")

            if len(empty_dirs) != 0:
                print("Removing empty directories...")

            for empty_dir in empty_dirs:
                os.system(f"rm -rf {empty_dir}")

            jobs += empty_jobs

        if self.retry_missing:
            print("Retrying missing jobs...")
            try:
                missing_jobs = self._get_missing_jobs()
            except Exception as e:
                print(f"Failed to get missing jobs with exception: {e}")
                missing_jobs = []

            if len(missing_jobs) == 0:
                print("No missing jobs found!")

            jobs += missing_jobs

        if retry and len(jobs) == 0:
            print("No jobs to retry!")
            return None

        if retry:
            print(f"Will retry the following {len(jobs)} jobs: {jobs}")

        self._submit(n_jobs, jobs)

        return self


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Submit batch jobs to ARC using aCT.")

    parser.add_argument(
        "--jobs_dir",
        type=str,
        help="Directory containing .xrsl files.",
        default="batch/run_0",
    )
    parser.add_argument(
        "--cluster_lst",
        type=str,
        nargs="*",
        help="List of sites to use.",
        default=None,
    )
    parser.add_argument(
        "--retry_failed",
        type=lambda x: str(x).lower() == "true",
        help="Retry failed jobs.",
        default=False,
    )
    parser.add_argument(
        "--retry_stuck",
        type=lambda x: str(x).lower() == "true",
        help="Retry stuck jobs.",
        default=False,
    )
    parser.add_argument(
        "--retry_empty",
        type=lambda x: str(x).lower() == "true",
        help="Retry empty jobs.",
        default=False,
    )
    parser.add_argument(
        "--retry_missing",
        type=lambda x: str(x).lower() == "true",
        help="Retry missing jobs.",
        default=False,
    )
    parser.add_argument(
        "--n_jobs",
        type=int,
        help="Number of jobs to submit.",
        default=None,
    )

    args = parser.parse_args()

    batch_submitter = ActBatchSubmitter(
        args.jobs_dir,
        args.cluster_lst,
        args.retry_failed,
        args.retry_stuck,
        args.retry_empty,
        args.retry_missing,
    )
    batch_submitter.submit(args.n_jobs)
