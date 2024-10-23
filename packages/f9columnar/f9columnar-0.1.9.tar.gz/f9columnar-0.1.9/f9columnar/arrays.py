import logging
from dataclasses import dataclass
from dataclasses import field as dataclass_field
from typing import List

import awkward as ak
import numpy as np

from f9columnar.processors import Processor
from f9columnar.utils.ak_helpers import check_list_type, check_numpy_type


@dataclass
class BaseArrays:
    array: ak.Array
    fields: list = dataclass_field(default_factory=list)

    def __post_init__(self):
        self.fields = self.array.fields

    @property
    def shape(self):
        return (len(self.array), len(self.fields))

    def mask(self, mask, inplace=True):
        if inplace:
            self.array = self.array[mask]
            return self
        else:
            return self.array[mask]

    def _check_type(self, array):
        raise NotImplementedError

    def __setitem__(self, field, new_array):
        if not self._check_type(new_array):
            raise ValueError(f"Field {field} is not of the correct type!")

        self.array[field] = new_array
        self.fields.append(field)

        return self

    def __getitem__(self, value):
        if type(value) is str:
            return self.array[value]
        elif type(value) is int:
            return self.array[value]
        elif type(value) is ak.Array or type(value) is np.ndarray:
            return self.mask(value)
        elif type(value) is slice:
            return self.array[value]
        else:
            raise ValueError("Value must be a field name or an array mask!")

    def __len__(self):
        return len(self.array)

    def __delitem__(self, field):
        self.array = ak.without_field(self.array, field)
        self.fields.remove(field)
        return self


@dataclass
class FlatArrays(BaseArrays):
    def _check_type(self, array):
        return check_numpy_type(array)

    def __str__(self):
        return f"{self.__class__.__name__}(shape={self.shape})"


@dataclass
class JaggedArrays(BaseArrays):
    def _check_type(self, array):
        return check_list_type(array)

    def _get_non_empty_mask(self):
        return ak.num(self.array[self.fields[0]]) > 0

    def remove_empty(self):
        mask = self._get_non_empty_mask()
        self.mask(mask, inplace=True)
        return self

    def __str__(self):
        return f"{self.__class__.__name__}(shape={self.shape})"


@dataclass
class Arrays:
    """This class is used to store flat and jagged arrays separately. It is used to store awkward arrays in a more
    structured way. It is initialized in the `ArrayProcessor` to separate flat and jagged fields. The funconality is
    similar to `ak.Array` but with seperate handling of flat and jagged arrays. It is intended to make it easier to
    work with ntuples that contain both flat (e.g. MC weights) and jagged fields (e.g. pt).

    Parameters
    ----------
    flat_arrays : FlatArrays
        Flat arrays.
    jagged_arrays : JaggedArrays
        Jagged arrays.

    Other Parameters
    ----------------
    flat_fields : list
        List of flat fields.
    jagged_fields : list
        List of jagged fields.
    fields : list
        List of all fields.

    Attributes
    ----------
    shape : tuple
        Shape of the arrays (number of events, number of flat array, number of jagged arrays).

    Methods
    -------
    update_fields()
        Update flat and jagged fields on (or after) initialization.
    mask_flat(mask, inplace=True)
        Mask flat arrays.
    mask_jagged(mask, inplace=True)
        Mask jagged arrays.
    remove_empty(inplace=True, return_mask=False)
        Remove empty sub arrays.

    Warning
    -------
    Masking is done inplace by default using `__setitem__`. To return a masked array, set `inplace=False` and use
    `mask_flat` or `mask_jagged` methods.

    Note
    ----
    To delete a field, use `del arrays[field]` syntax.

    """

    flat_arrays: FlatArrays
    jagged_arrays: JaggedArrays

    flat_fields: List[str] = dataclass_field(default_factory=list)
    jagged_fields: List[str] = dataclass_field(default_factory=list)
    fields: List[str] = dataclass_field(default_factory=list)

    def __post_init__(self):
        self.update_fields()

    def update_fields(self):
        self.flat_fields = self.flat_arrays.fields
        self.jagged_fields = self.jagged_arrays.fields
        self.fields = self.flat_fields + self.jagged_fields
        return self

    @property
    def shape(self):
        return (len(self), len(self.flat_fields), len(self.jagged_fields))

    def mask_flat(self, mask, inplace=True):
        if inplace:
            self.flat_arrays.mask(mask, inplace=True)
            self.jagged_arrays.mask(mask, inplace=True)
            return self
        else:
            return self.flat_arrays.mask(mask, inplace=False), self.jagged_arrays.mask(mask, inplace=False)

    def mask_jagged(self, mask, inplace=True):
        if inplace:
            self.jagged_arrays.mask(mask, inplace=True)
            return self
        else:
            return self.jagged_arrays.mask(mask, inplace=False)

    def remove_empty(self, inplace=True, return_mask=False):
        non_empty_mask = self.jagged_arrays._get_non_empty_mask()
        if return_mask:
            return self.mask_flat(non_empty_mask, inplace=inplace), non_empty_mask
        else:
            return self.mask_flat(non_empty_mask, inplace=inplace)

    def __setitem__(self, field, new_array):
        if check_numpy_type(new_array):
            self.flat_arrays[field] = new_array
        elif check_list_type(new_array):
            self.jagged_arrays[field] = new_array
        else:
            raise ValueError("Array is not of the correct type!")

        self.update_fields()

        return self

    def _get_by_field(self, field):
        if field in self.flat_fields:
            return self.flat_arrays[field]
        elif field in self.jagged_fields:
            return self.jagged_arrays[field]
        else:
            raise KeyError(f"Field {field} not found in flat or jagged fields!")

    def _get_by_slice(self, slice_idx):
        return self.flat_arrays[slice_idx], self.jagged_arrays[slice_idx]

    def _get_by_mask(self, mask):
        if check_numpy_type(mask):
            self.mask_flat(mask, inplace=True)
        elif check_list_type(mask):
            self.mask_jagged(mask, inplace=True)
        else:
            raise ValueError("Mask is not of the correct type!")

        return self

    def __getitem__(self, value):
        if type(value) is str:
            return self._get_by_field(value)
        elif type(value) is int:
            return self._get_by_slice(value)
        elif type(value) is ak.Array or type(value) is np.ndarray:
            return self._get_by_mask(value)
        elif type(value) is slice:
            return self._get_by_slice(value)
        else:
            raise ValueError("Value must be a field name, int, array mask or slice!")

    def __len__(self):
        len_flat, len_jagged = len(self.flat_arrays), len(self.jagged_arrays)
        assert len_flat == len_jagged, "Flat and jagged arrays have different lengths!"
        return len_flat

    def __delitem__(self, field):
        if field in self.flat_fields:
            del self.flat_arrays[field]
        elif field in self.jagged_fields:
            del self.jagged_arrays[field]
        else:
            raise KeyError(f"Field {field} not found in flat or jagged fields!")

        self.fields.remove(field)

        return self

    def __str__(self):
        return f"{self.__class__.__name__}(shape={self.shape})"


class ArrayProcessor(Processor):
    def __init__(self):
        """Processor to separate flat and jagged fields into two arrays from an awkward array.

        Note
        ----
        This will modify the input arrays. It is intended to be used as the first processor in the analysis chain in
        the case of ntuples that contain both flat and jagged fields.

        """
        super().__init__(name="arrayProcessor")
        self.flat_fields, self.jagged_fields, self.other_fields = [], [], []

    def _get_fields(self, arrays):
        arrays_contents = arrays.type.content.contents
        arrays_fields = arrays.type.content.fields

        for content, array_field in zip(arrays_contents, arrays_fields):
            if isinstance(content, ak.types.NumpyType):
                self.flat_fields.append(array_field)
            elif isinstance(content, ak.types.ListType):
                self.jagged_fields.append(array_field)
            else:
                self.other_fields.append(array_field)

        if len(self.other_fields) != 0:
            logging.warning(f"Fields {self.other_fields} are not flat or jagged! Will not be processed.")

        return self.flat_fields, self.jagged_fields

    def run(self, arrays):
        self._get_fields(arrays)

        flat_arrays, jagged_arrays = arrays[self.flat_fields], arrays[self.jagged_fields]

        arrays = Arrays(FlatArrays(flat_arrays), JaggedArrays(jagged_arrays))

        return {"arrays": arrays}
