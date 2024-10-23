# F9 Columnar

### 🚧 **Work in Progress** ⚠️

##  Setup

### User install

#### With PyTorch GPU

```shell
pip install f9columnar[torch]
```

#### With PyTorch CPU

```shell
pip install f9columnar
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

#### Without PyTorch

```shell
pip install f9columnar
```

### Development install

Use [poetry](https://python-poetry.org/) to install the required packages:

```shell
poetry config cache-dir $PWD
poetry config virtualenvs.in-project true
poetry install -E torch
```

This environment is duplicated for batch processing on dCache using `batch_requirements.txt`.

### aCT

[ARC](https://doc.vega.izum.si/arc) Control Tower (aCT) is a system for submitting and managing payloads on ARC (and other) Computing Elements. It is used to submit jobs on sites in Slovenia.

#### Configuration

Common aCT config is provided in [`config/act-client/config.yaml`](columnar/submit/config/act-client/config.yaml). To use it, copy the file to `~/.config/act-client/config.yaml`.

#### Installation

First get the python binary path from the environment you use using `which python`.

Make the virtual environment using this binary:

```shell
/cvmfs/sft.cern.ch/lcg/views/LCG_104b/x86_64-el9-gcc13-opt/bin/python3 -m venv act_venv
```

In the newly created environment install [aCT](https://github.com/ARCControlTower/aCT):

```shell
source act_venv/bin/activate
pip install "git+https://github.com/ARCControlTower/aCT.git@test#subdirectory=src/act/client/aCT-client"
pip install pandas
```

The command `act` is available in `PATH` as the virtual environment is activated.

#### Voms proxy setup

Note that it is recommended to be in `/atlas/si` group and make the proxy with it. Active it using (in a separate terminal):

```shell
setupATLAS
lsetup emi
voms-proxy-init --valid 96:0 --voms atlas:/atlas/si
```

To propagate the proxy to the system use

```shell
act proxy
```

At this point you are ready to use aCT.

#### Analysis specific setup

For job submission, the aCT environment must be setup. The following commands will activate the environment and alias `act_submit`, `act_get` and `act_monitor` python scripts:

```shell
source setup_act.sh
```

- `act_submit` - submit jobs
  - `--jobs_dir` (default: `batch/run_0`)
  - `--cluster_lst` (default: everything in `config`)
  - `--retry_failed` (default: `False`)
  - `--retry_stuck` (default: `False`)
  - `--retry_empty` (default: `False`)
  - `--retry_missing` (default: `False`)
- `act_get` - download done jobs
  - `--jobs_dir` (default: `batch/run_0`)
  - `--retry_empty` (default: `True`)
  - `--include_finishing` (default: `False`)
- `act_monitor` - monitor jobs

#### General commands

Most commands accept either job ID using `-i <ID>` or a full list is toggled using `-a` and can be filtered by job name using `-n <NAME>` (partial match is also available). Please consult the help for each command.

The following commands are useful (see `act --help` for more):

- `act stat` - list all jobs and their statuses
- `act cat` - show job log (works also while job is running)
- `act kill` - kill selected jobs
- `act clean` - clean selected jobs, mainly used after killing
- `act resub` - resubmit selected jobs if failed due to a glitch
- `act get --noclean` - get the output of selected jobs without cleaning the job

## Getting started example

### Basic example

The main idea is to have a columnar event loop that returns arrays of events. The code and usage is the same as in a standard torch training loop over epochs, but instead of having epochs we iterate over batches of events.

```python
from f9columnar.root_dataloader import get_root_dataloader

def filter_branch(branch):
    # select only these two branches
    return branch.name == "tau_p4" or branch.name == "lephad_p4"

# root_dataloader is an instance of a torch DataLoader that uses an IterableDataset
root_dataloader, total = get_root_dataloader(
    ntuple_path, # path to the root file (file, list of paths or directory)
    name="data", # name identifier
    chunks="auto", # number of chunks to split the root file(s) into
    setup_workers=4, # number of workers for initial setup
    step_size="15 MB", # size of the step for the worker to read the root file
    postifx="NOMINAL", # root file postfix
    filter_branch=filter_branch, # filter branches
    processors=None, # arbitrary calculations on arrays
    num_workers=12, # number of workers for parallel processing
)

# loop over batches of events from .root file(s), each batch is an awkward array
for events in root_dataloader:
    arrays, report = events
    # ... do something with the arrays
```

Doing calculations on arrays inside of workers can be done using a `Processor`. Many processors can be chained together into a `ProcessorsGraph` (DAG) to perform more complex calculations. Processors are applied to the arrays in the order given by the topological sort of the DAG. Note that each worker runs the same processor graph on batches of array events and returns the result to the event loop when done. So in the above example there would be 12 (`num_workers`) processor graphs running in parallel on small batches of events. An example of calculating tau visible mass and then applying a cut on this variable is shown below.

```python
from f9columnar.processor import ProcessorsGraph, CheckpointProcessor
from f9columnar.object_collections import Variable, VariableCollection, Cut, CutCollection
from f9columnar.histograms import HistogramProcessor

class VisibleMass(Variable): # Variable is a Processor
    name = "vis_mass" # processor name
    branch_name = "lephad_p4" # name of the branch in the .root file

    def __init__(self):
        super().__init__()

    def run(self, arrays): # each processor must implement a run method
        lephad_p4 = arrays[self.branch_name] # branch_name is the name of the field in the ak array
        v = get_kinematics_vector(lephad_p4) # use vector with px, py, pz and E

        arrays["tau_vis_mass"] = v.m # add a new field to the arrays

        return {"arrays": arrays} # return the arrays (can also return None if no changes are made)

class CutVisibleMass(Cut): # Cut is a Processor
    name = "vis_mass_cut"
    branch_name = None # is not a branch in ntuples but was defined in the VisibleMass processor

    def __init__(self, cut_lower, cut_upper): # argumnets of the processor
        super().__init__()
        self.cut_lower = cut_lower
        self.cut_upper = cut_upper

    def run(self, arrays):
        mask = (arrays["tau_vis_mass"] > self.cut_lower) & (arrays["tau_vis_mass"] < self.cut_upper)
        arrays = arrays[mask] # apply the cut

        return {"arrays": arrays} # return must be a dictionary with key name for the argument of the next processor

class Histograms(HistogramProcessor):
    def __init__(self, name="histograms"):
        super().__init__(name)

        self.make_hist1d("tau_vis_mass", 20, 80.0, 110.0) # make a histogram with 20 bins from 80 to 110 GeV

    def run(self, arrays):
        return super().run(arrays) # auto fills histograms if array names match histogram names

var_collection = VariableCollection(VisibleMass, init=False) # will initialize later
cut_collection = CutCollection(CutVisibleMass, init=False)

collection = var_collection + cut_collection # add collections of objects together
branch_filter = collection.branch_name_filter # defines the branches that the processors depend on

graph = ProcessorsGraph() # graph has a fit method that gets called inside the root_dataloader

# add nodes to the graph
graph.add(
    CheckpointProcessor("input"), # input node
    var_collection["vis_mass"](), # initialize the processor
    cut_collection["vis_mass_cut"](cut_lower=90.0, cut_upper=100.0),
    CheckpointProcessor("output", save_arrays=True), # saves final arrays
    Histograms(),
)

# build a processor graph
graph.connect(
    [
        ("input", "vis_mass"),
        ("vis_mass", "vis_mass_cut"),
        ("vis_mass_cut", "output"),
        ("output", "histograms"),
    ]
)

# plot the graph
graph.draw("graph.pdf")

# ... pass into the root_dataloader with the processors argument (e.g. processors=graph)
# in this case the dataloader will return a fitted graph
for processed_graph in dataloader:
    histograms = processed_graph["histograms"].hists
    arrays = processed_graph["output"].arrays
    # ... do something with the histograms and arrays
```

### Ntuple analysis example

TODO

### ROOT DataLoader schema

![ROOT_dl](https://i.imgur.com/dGU2xDL.png)

## Development

### Making a portable venv with conda

Make sure you have [Miniconda](https://docs.anaconda.com/miniconda/) installed:

```shell
mkdir miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3/miniconda.sh
bash miniconda3/miniconda.sh -b -u -p miniconda3
rm -rf miniconda3/miniconda.sh
miniconda3/bin/conda init bash
```

`init` command will add some path variables to your `~/.bashrc` that you can delete when done.

To test conda install use:

```shell
conda -V
```

Next, make a virtual environment and install the required packages:

```shell
conda create -n batch_venv python=3.12.4
source activate batch_venv
pip install -r batch_requirements.txt
```

In order to make this environment portable use [conda-pack](https://conda.github.io/conda-pack/):

```shell
conda install conda-pack
conda pack
conda deactivate
```

On remote machine unpack the environment:

```shell
tar -xzf batch_venv.tar.gz
source batch_venv/bin/activate
conda-unpack
```

If there are problems with the `.gz` file, unpack it and tar it again without compression:

```shell
mkdir -p batch_venv
tar -xzf batch_venv.tar.gz -C batch_venv
tar -cvf batch_venv.tar batch_venv
```

### dCache

Basic instructions can be found [here](https://doc.sling.si/en/navodila/podatki/).

To upload the above described venv to dCache use:

```shell
arccp batch_venv.tar davs://dcache.sling.si:2880/atlas/jang/
```

where you can make your own directory with `arcmkdir`.

### lxplus venv setup

Log into lxplus:
```shell
ssh <name>@lxplus.cern.ch
```

Since we want custom python packages and installing on `afs` is not recommended, we will use `eos`:
```shell
cd /eos/user/j/jgavrano
```

Source an LCG release to use as base:
```shell
setupATLAS
lsetup "views LCG_105b x86_64-el9-gcc13-opt"
```

Setup `venv` and install required packages from `requirements`:
```shell
PYTHONUSERBASE=/eos/user/j/jgavrano/F9Columnar/ pip3 install --user --no-cache-dir -r requirements.txt
```

Test with libraries in `eos`:
```shell
PYTHONPATH=/eos/user/j/jgavrano/F9Columnar/lib/python3.9/site-packages/:$PYTHONPATH python3 <script_name>.py
```

Setup python with custom `venv`:
```shell
export PYTHONPATH=/eos/user/j/jgavrano/F9Columnar/lib/python3.9/site-packages/:$PYTHONPATH
```

To make it public go to cernbox website and share it with `atlas-current-physicists`.
