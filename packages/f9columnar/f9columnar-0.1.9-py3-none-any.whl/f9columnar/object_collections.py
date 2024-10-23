import copy
import time
from abc import abstractmethod
from collections import OrderedDict

from f9columnar.processors import Processor


class ObjectCollection:
    def __init__(self, collection_name, *objects, init=False):
        """Collection of objects.

        Parameters
        ----------
        collection_name : str
            Name of this collection.
        objects : *args
            obj objects to store.
        init : bool
            Whether to initialize the objects or not.
        """
        self.name = collection_name
        self.init = init
        self.objects = OrderedDict()

        for obj in objects:
            if init:
                obj = obj()
                self.objects[obj.name] = obj
            else:
                self.objects[obj.name] = obj

        self.branch_names = self._get_branch_names()

    def __getitem__(self, name):
        return self.objects[name]

    def __add__(self, obj):
        if isinstance(obj, ObjectCollection):
            for v in obj.objects.values():
                if v in self.objects:
                    raise ValueError(f"Object {v.name} already exists in the {self.collection_name} collection!")
                else:
                    self.objects[v.name] = v
        else:
            if obj in self.objects:
                raise ValueError(f"Object {obj.name} already exists in the {self.collection_name} collection!")
            else:
                if self.init:
                    obj = obj()
                    self.objects[obj.name] = obj
                else:
                    self.objects[obj.name] = obj

        self.branch_names = sorted(list(set(self._get_branch_names())))

        return self

    def _get_branch_names(self):
        branch_names = []
        for v in self.objects.values():
            if not hasattr(v, "branch_name"):
                continue

            branch_name = v.branch_name

            if branch_name is None:
                continue
            elif type(branch_name) is list:
                branch_names += [br for br in branch_name if br is not None]
            else:
                branch_names.append(v.branch_name)

        return branch_names

    def branch_name_filter(self, branch):
        if branch.name in self.branch_names:
            return True
        else:
            return False

    def as_list(self):
        return list(self.objects.values())

    def __str__(self):
        str_output = f"Object Collection\n{17 * '-'}\n"

        for name, obj in self.objects.items():
            str_output += f"{name}: {str(obj)}\n"

        return str_output[:-1]


class Variable(Processor):
    name = None
    branch_name = None

    def __init__(self):
        super().__init__(self.name)

    @abstractmethod
    def run(self):
        pass


class VariableCollection(ObjectCollection):
    def __init__(self, *variables, init=False):
        super().__init__("Variables", *variables, init=init)


class Cut(Processor):
    name = None
    branch_name = None

    def __init__(self):
        super().__init__(self.name)
        self.start_n, self.end_n = None, None

    def _run(self, arrays, **kwargs):
        self.start_n, start_time = len(arrays), time.time()

        arrays, kwargs = copy.deepcopy(arrays), copy.deepcopy(kwargs)
        self._results = self.run(arrays, **kwargs)

        self.end_n, self.delta_time = len(self._results["arrays"]), time.time() - start_time

        return self

    @abstractmethod
    def run(self):
        pass


class CutCollection(ObjectCollection):
    def __init__(self, *cuts, init=False):
        super().__init__("Cuts", *cuts, init=init)


class Weight(Processor):
    name = None
    branch_name = None

    def __init__(self):
        """MC weights processor.

        References
        ----------
        [1] - https://ipnp.cz/scheirich/?page_id=292

        """
        super().__init__(self.name)

    @abstractmethod
    def run(self):
        pass


class WeightCollection(ObjectCollection):
    def __init__(self, *weights, init=False):
        super().__init__("Weights", *weights, init=init)


class HistogramCollection(ObjectCollection):
    def __init__(self, *histograms, init=False):
        super().__init__("Histograms", *histograms, init=init)
