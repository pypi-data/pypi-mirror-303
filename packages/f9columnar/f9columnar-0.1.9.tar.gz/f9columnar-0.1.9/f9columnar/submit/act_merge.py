import argparse
import glob
import os

from f9columnar.utils.helpers import dump_pickle, load_pickle


class ActMerger:
    def __init__(self, jobs_dir, save=True):
        self.jobs_dir = jobs_dir
        self.save = save

    def merge(self):
        out_dir = f"{self.jobs_dir}/out"

        dirs = [f.path for f in os.scandir(out_dir) if f.is_dir()]
        print(f"Found {len(dirs)} output directories.")

        output_pickles, dataset_pickles = [], []
        for d in dirs:
            p_files = glob.glob(f"{d}/*.p")

            output_pickles.append([])

            for p_file in p_files:
                if "_dataset" in p_file:
                    dataset_pickles.append(p_file)
                else:
                    output_pickles[-1].append(p_file)

            if len(output_pickles[-1]) == 0:
                print(f"No output pickles found in {d}. Will remove directory!")
                os.system(f"rm -r {d}")

        assert len(output_pickles) == len(dataset_pickles), "Number of output and dataset pickles do not match!"
        assert len(dirs) == len(output_pickles), "Number of directories and pickles do not match!"

        merged_outputs, merged_datasets = {}, {}

        already_present = set()
        for output_pickles_lst, dataset_pickle in zip(output_pickles, dataset_pickles):

            check_present = os.path.basename(dataset_pickle)
            if check_present in already_present:
                continue
            else:
                already_present.add(check_present)

            for f_name in output_pickles_lst:
                key = os.path.basename(f_name)[:-2]
                if key not in merged_outputs:
                    merged_outputs[key] = []

                merged_outputs[key].append(load_pickle(f_name))

            key = os.path.basename(dataset_pickle)[:-2]
            if key not in merged_datasets:
                merged_datasets[key] = []

            merged_datasets[key].append(load_pickle(dataset_pickle))

        for k in merged_outputs.keys():
            print(f"Found {len(merged_outputs[k])} outputs for {k}.")

        if self.save:
            print(f"Saving merged outputs to {out_dir}/merged_outputs.p.")
            dump_pickle(f"{out_dir}/merged_outputs.p", {"outputs": merged_outputs, "datasets": merged_datasets})

        return merged_outputs, merged_datasets


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch merger.")

    parser.add_argument(
        "--jobs_dir",
        type=str,
        help="Directory containing .xrsl files.",
        default="batch/run_0",
    )
    args = parser.parse_args()

    act_merger = ActMerger(args.jobs_dir)
    act_merger.merge()
