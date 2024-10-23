import copy
import logging
import os
import time
from abc import ABC, abstractmethod
from functools import reduce

import networkx as nx

from f9columnar.plotting import handle_plot_exception


class ProcessorsGraph:
    def __init__(self, copy_processors=True, prune_results=True, identifier=""):
        """Direct Acyclic Graph (DAG) composer for processors. Each node is executed sequentially by the `fit` method
        in the order given by the topological sort of the graph. Processor node recieves the results of its predecessors
        as input arguments (note that the args order is given by the topological sort).

        Parameters
        ----------
        copy_processors : bool
            Flag to copy processors on each fit. Should generally be set to True to avoid side effects.
        identifier : str
            Identifier string to add to all node names, by default "".
        prune_results : bool
            Flag to prune results of the processors after each fit. Prune removes _results from the processor if all
            its dependencies (all the connected nodes that are not needed anymore) are met.

        Other parameters
        ----------------
        processors : dict
            Dictionary of processors objects.
        processors_edges : list of size 2 tuples of str
            List of edges connecting processors nodes.
        graph : nx.DiGraph
            NetworkX directed graph object.
        topo_sorted : list of str
            List of topologically sorted nodes.

        Methods
        -------
        add(*processors)
            Add processors nodes to the graph.
        connect(processor_edges=None)
            Connect processors nodes given edges. If no edges are given, the previously connected edges are used.
        chain()
            Connect processors nodes in a chain (linear order).
        extend(other_graph, extend_node)
            Extend the graph with another graph starting from a node.
        insert(other_graph, insert_node)
            Insert another graph into the graph starting from a node and then reconnecting.
        fit(arrays, reports, event_iterator_worker, **kwargs)
            Fit the processors in the graph.
        style_graph(fillcolor)
            Style the graph. Should be called before draw. Needs pygraphviz installed.
        draw(file_path, fontsize=10, jupyter=False, **kwargs)
            Draw the graph and save it to a file.

        Example
        -------

               | --- p2 --- |
        p1 --- |            | --- p4
               | --- p3 --- |

        graph = ProcessorsGraph()

        p1 = Proc1(name="p1", arg1="foo")
        p2 = Proc2(name="p2", arg2="bar")
        p3 = Proc3(name="p3")
        p4 = Proc4(name="p4")

        graph.add(p1, p2, p3, p4)
        graph.connect([("p1", "p2"), ("p1", "p3"), ("p2", "p4"), ("p3", "p4")])
        graph.fit()

        References
        ----------
        [1] - https://networkx.org/documentation/stable/reference/algorithms/dag.html
        [2] - https://networkx.org/nx-guides/content/algorithms/dag/index.html
        [3] - https://graphviz.org/doc/info/attrs.html
        [4] - https://graphviz.org/docs/layouts/
        [5] - https://github.com/bermanmaxim/Pytorch-DAG

        """
        self.copy_processors = copy_processors
        self.prune_results = prune_results
        self.identifier = identifier

        self.processors = {}
        self.processors_edges = []
        self.graph = nx.DiGraph()
        self.topo_sorted = None

        self._node_predecessors, self._node_successors, self._dependencies = None, None, None

    def __getitem__(self, name):
        return self.processors[name]

    @property
    def last_node(self):
        nodes = [node for node in self.graph.nodes() if self.graph.out_degree(node) == 0]
        if len(nodes) == 1:
            return nodes[0]
        else:
            return nodes

    def add(self, *processors):
        for processor in processors:
            if processor.name not in self.processors:
                name = f"{processor.name}{self.identifier}"
                self.processors[name] = processor
                processor.name = name
            else:
                raise ValueError(f"Node with name {processor.name} already exists. Node names must be unique!")

        return self

    def __add__(self, other):
        if type(other) is list:
            return self.add(*other)
        else:
            return self.add(other)

    def connect(self, processor_edges=None):
        if processor_edges is None:
            assert self.processors_edges, "No edges to connect processors!"
            processor_edges = self.processors_edges
        else:
            if len(self.processors_edges) != 0:
                self.processors_edges += processor_edges
            else:
                self.processors_edges = processor_edges

        for edge in processor_edges:
            parent, child = edge[0], edge[1]

            if parent not in self.graph:
                self.graph.add_node(parent)

            if child not in self.graph:
                self.graph.add_node(child)

            self.graph.add_edge(parent, child)

        assert nx.is_directed_acyclic_graph(self.graph), "Graph is not a DAG!"

        self.topo_sorted = list(nx.topological_sort(self.graph))

        logging.debug(f"Topological sort: {self.topo_sorted}")

        self._node_predecessors = {name: list(self.graph.predecessors(name)) for name in self.topo_sorted}
        self._node_successors = {name: list(self.graph.successors(name)) for name in self.topo_sorted}
        self._dependencies = {name: set(self._node_successors[name]) for name in self.topo_sorted}

        return self

    def chain(self):
        processor_names = [name for name in self.processors.keys()]

        chain = []
        for i in range(1, len(processor_names)):
            chain.append((processor_names[i - 1], processor_names[i]))

        self.processors_edges += chain
        self.connect()

        return self

    def _validate_nodes(self, other_graph):
        self_names = [name for name in self.processors.keys()]
        other_names = [name for name in other_graph.processors.keys()]

        for self_name in self_names:
            if self_name in other_names:
                raise ValueError(f"Found duplicate node {self_name} graphs. Node names must be unique!")

        return True

    def _extend_edges(self, other_graph, extend_node, return_extend_idx=False):
        self._validate_nodes(other_graph)

        self_edges, other_edges = self.processors_edges, other_graph.processors_edges

        extend_idx = []
        for i, edge in enumerate(self_edges):
            if edge[1] == extend_node:
                extend_idx.append(i)

        assert len(extend_idx) == 1, f"Found {len(extend_idx)} extendable nodes in graph. Must be exactly 1!"
        extend_idx = extend_idx[0]

        new_edges = copy.deepcopy(self_edges)
        new_edges.insert(extend_idx + 1, (self_edges[extend_idx][1], other_edges[0][0]))
        new_edges[extend_idx + 2 : extend_idx + 2] = other_edges

        if return_extend_idx:
            return new_edges, extend_idx
        else:
            return new_edges

    def _insert_edges(self, other_graph, insert_node):
        new_edges, extend_idx = self._extend_edges(other_graph, insert_node, return_extend_idx=True)

        connect_idx = extend_idx + len(other_graph) + 2
        new_edges.insert(connect_idx, (other_graph[-1][1], new_edges[connect_idx][0]))

        return new_edges

    def extend(self, other_graph, extend_node):
        new_edges = self._extend_edges(other_graph, extend_node)
        new_graph = self.__class__(copy_processors=self.copy_processors)

        new_graph.add(*self.processors.values(), *other_graph.processors.values())
        new_graph.connect(new_edges)

        return new_graph

    def insert(self, other_graph, insert_node):
        new_edges = self._insert_edges(other_graph, insert_node)
        new_graph = self.__class__(copy_processors=self.copy_processors)

        new_graph.add(*self.processors.values(), *other_graph.processors.values())
        new_graph.connect(new_edges)

        return new_graph

    def fit(self, *args, **kwargs):
        if self.copy_processors:
            processors = copy.deepcopy(self.processors)
        else:
            processors = self.processors

        previous_nodes = set()
        for i, node in enumerate(self.topo_sorted):
            processor = processors[node]

            processor.previous_processors = {name: processors[name] for name in previous_nodes}
            previous_nodes.add(processor.name)

            logging.debug(f"Running node {node} at step {i}.")

            if i == 0:
                processor._run(*args, **kwargs)
            else:
                inputs = [processors[name]._results for name in self._node_predecessors[node]]
                input_args = list(filter(None, inputs))

                if len(input_args) == 0:
                    processor._run(*inputs)
                else:
                    input_kwargs = reduce(lambda a, b: {**a, **b}, input_args)
                    processor._run(**input_kwargs)

                if self.prune_results:
                    for prune_node, prune_node_dependencies in self._dependencies.items():
                        if len(prune_node_dependencies) == 0 or processors[prune_node]._results is None:
                            continue
                        if prune_node_dependencies.issubset(previous_nodes):
                            processors[prune_node]._results = None
                            logging.debug(f"Pruning node {prune_node} from node {node} at step {i}.")

        return processors

    def style_graph(self, fillcolor):
        for node in self.graph.nodes:
            self.graph.nodes[node]["fillcolor"] = fillcolor
            self.graph.nodes[node]["style"] = "filled"
        return self

    @handle_plot_exception
    def draw(self, file_path, fontsize=10, jupyter=False, **kwargs):
        A = nx.nx_agraph.to_agraph(self.graph)
        A.graph_attr.update(fontsize=fontsize, **kwargs)
        A.layout(prog="dot")

        if jupyter:
            from IPython.core.display import SVG, display

            A.draw(file_path, format="svg")
            display(SVG(file_path))
        else:
            A.draw(file_path, format="pdf")

        logging.info(f"Saved graph to {file_path}")

        return A.to_string()


class Processor(ABC):
    def __init__(self, name):
        """Base class for processors. All processors should inherit from this class. Run method gets called in the `fit`
        method of the ProcessorsGraph.

        Parameters
        ----------
        name : str
            Name of the processor.

        Other parameters
        ----------------
        worker_id : int
            Initialized by Dataloader.
        previous_processors : dict
            Predecessors of this processor in the DAG.
        _results : list
            Results of the processor.

        Note
        ----
        Run is executed inside the ROOTLoaderGenerator after batch arrays have been collected by the uproot iterartor.

        """
        self.name = name

        self.worker_id = None
        self.previous_processors = None
        self.delta_time = None
        self._results = None

    @abstractmethod
    def run(self, *args, **kwargs):
        """Needs to be implemented by every processor object. Must return a dictionary with keys for argument names!"""
        pass

    def _run(self, *args, **kwargs):
        """Internal run method."""
        start_time = time.time()

        args, kwargs = copy.deepcopy(args), copy.deepcopy(kwargs)
        self._results = self.run(*args, **kwargs)

        self.delta_time = time.time() - start_time

        return self

    @property
    def reports(self):
        return self.previous_processors["input"]._reports

    @property
    def is_data(self):
        return self.previous_processors["input"]._reports[0]["is_data"]


class CheckpointProcessor(Processor):
    def __init__(self, name, save_arrays=False, save_event_iterator_worker=False):
        """Checkpoint processor that acts as input/output node for the ProcessorsGraph. Also used to save arrays at nodes.

        Parameters
        ----------
        name : str
            Name of the processor.
        save_arrays : bool
            Flag to save arrays at this node.
        save_event_iterator_worker : bool
            Flag to return the event iterator worker for debugging purposes.

        Other parameters
        ----------------
        reports : list of dict
            Reports returned by the ROOTLoaderGenerator.
        n_events : int
            Number of events in the arrays.
        arrays : ak.Array
            Arrays at this node.

        """
        super().__init__(name)
        self.save_arrays = save_arrays
        self.save_event_iterator_worker = save_event_iterator_worker

        self.arrays = None
        self._reports = None
        self.event_iterator_worker = None

        self.n_events = None

    def run(self, arrays, reports=None, event_iterator_worker=None):
        self._reports = reports
        self.n_events = len(arrays)

        if self.save_arrays:
            self.arrays = arrays

        if self.save_event_iterator_worker:
            self.event_iterator_worker = event_iterator_worker

        return {"arrays": arrays}


class PostprocessorsGraph(ProcessorsGraph):
    def __init__(self):
        """Postprocessors graph to process the results of the processors.

        Note
        ----
        Takes the fitted processors dictionary returned by the ProcessorsGraph and processes it. The key difference is
        that the PostprocessorsGraph does not copy its processors allowing for the accumulation of results in each
        postprocessor. This is useful for plotting and saving results. Note that this does not allow for
        multiprocessing.

        """
        super().__init__()
        self.copy_processors = False

    def fit(self, input_processors, *args, **kwargs):
        return super().fit(input_processors, *args, **kwargs)


class Postprocessor(ABC):
    def __init__(self, name, save_path=None):
        """Postprocessor base class. All postprocessors should inherit from this class.

        Parameters
        ----------
        name : str
            Name of the postprocessor.
        save_path : str, optional
            Path with file name to save the postprocessor results in the save method, by default None.
        """
        super().__init__()
        self.name = name

        if save_path is not None:
            os.makedirs("/".join(save_path.split("/")[:-1]), exist_ok=True)
        self.save_path = save_path

        self.previous_processors = None
        self._results = None

    @abstractmethod
    def run(self, *args, **kwargs):
        """Needs to be implemented by every postprocessor object."""
        pass

    def _run(self, *args, **kwargs):
        """Internal run method."""
        args, kwargs = copy.deepcopy(args), copy.deepcopy(kwargs)
        self._results = self.run(*args, **kwargs)
        return self

    def save(self):
        """Save results of the postprocessor."""
        pass

    @property
    def is_data(self):
        return self.previous_processors["input"]._is_data


class CheckpointPostprocessor(Postprocessor):
    def __init__(self, name, save_input_processors=False):
        """Checkpoint postprocessor."""
        super().__init__(name)
        self.save_input_processors = save_input_processors

        self.input_processors, self._is_data = [], None

    def run(self, processors, is_data=None):
        if self.save_input_processors:
            self.input_processors.append(processors)

        self._is_data = is_data

        return {"processors": processors}
