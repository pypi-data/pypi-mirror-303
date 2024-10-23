import awkward as ak
import numpy as np
import vector
from numba import njit


def ak_replace(array, replace_dct):
    """https://stackoverflow.com/questions/65729150/efficient-method-to-replace-values-in-awkward-array-according-to-a-dictionary"""
    flattened, num = ak.flatten(array), ak.num(array)

    keys = ak.Array(replace_dct.keys())
    values = ak.Array([replace_dct[key] for key in keys])

    lookup_index = np.searchsorted(np.asarray(keys), np.asarray(flattened), side="left")

    return ak.unflatten(values[keys[lookup_index]], num)


def ak_leading(array):
    idx = ak.argsort(abs(array), axis=1, ascending=False)
    return ak.fill_none(ak.firsts(array[idx]), np.float32(np.nan))


@njit
def _get_subleading(sorted_array):
    subleading_array = np.empty(len(sorted_array))

    for i, sub_array in enumerate(sorted_array):
        if len(sub_array) == 1:
            subleading_array[i] = sub_array[0]
        else:
            subleading_array[i] = sub_array[1]

    return subleading_array


def ak_subleading(array):
    assert not ak.any(ak.num(array) == 0), "Arrays should not be empty."

    idx = ak.argsort(abs(array), axis=1, ascending=False)

    subleading_array = _get_subleading(array[idx])
    subleading_array = ak.Array(subleading_array)

    subleading_array = ak.fill_none(subleading_array, np.float32(np.nan))

    return subleading_array


def ak_dr(eta, phi):
    """Calculate delta R between leading and subleading objects in array."""

    mask_eta, mask_phi = ak.num(eta) >= 2, ak.num(phi) >= 2
    mask = mask_eta & mask_phi

    eta, phi = eta[mask], phi[mask]

    eta_leading, eta_subleading = ak_leading(eta), ak_subleading(eta)
    phi_leading, phi_subleading = ak_leading(phi), ak_subleading(phi)

    dR = ((eta_leading - eta_subleading) ** 2 + (phi_leading - phi_subleading) ** 2) ** 0.5

    return dR


@njit
def _get_unique(ak_arr_builder, ak_arr):
    for sub_arr in ak_arr:
        unique = np.unique(np.asarray(sub_arr))

        ak_arr_builder.begin_list()
        for u in unique:
            ak_arr_builder.append(u)
        ak_arr_builder.end_list()

    return ak_arr_builder


def ak_unique(ak_arr):
    ak_arr = ak.fill_none(ak_arr, [])

    builder = ak.ArrayBuilder()
    _get_unique(builder, ak_arr)

    array = builder.snapshot()
    return array


def ak_inv_mass(pt, eta, phi, m_value, return_zip=False):
    v = vector.zip(
        {
            "pt": pt,
            "eta": eta,
            "phi": phi,
            "m": ak.full_like(pt, m_value),
        },
    )

    if return_zip:
        return ak.sum(v, axis=1)
    else:
        return ak.to_numpy(ak.sum(v, axis=1).mass)


def ak_to_flat_jagged_arrays(arrays, flat_branches=None, is_flat_func=None):
    if flat_branches is None:
        flat_branches = []

    if is_flat_func is None:
        is_flat_func = lambda b: True if b in flat_branches else False

    fields = arrays.fields
    flat_fields = [field for field in fields if is_flat_func(field, flat_branches)]
    jagged_fields = [field for field in fields if field not in flat_fields]

    return arrays[flat_fields], arrays[jagged_fields]


def ak_combine_flat_jagged_arrays(flat_arrays, jagged_arrays):
    flat_arrays = {field: flat_arrays[field] for field in flat_arrays.fields}
    jagged_arrays = {field: jagged_arrays[field] for field in jagged_arrays.fields}

    arrays = ak.Array(flat_arrays | jagged_arrays)

    return arrays


def check_numpy_type(array, assert_1d=True):
    if type(array) is ak.Array and type(array.type.content) is ak.types.NumpyType:
        return True
    elif type(array) is np.ndarray:
        if assert_1d:
            assert array.ndim == 1, "Array must be 1D!"
        return True
    else:
        return False


def check_list_type(array):
    if type(array) is ak.Array and type(array.type.content) is ak.types.ListType:
        return True
    else:
        return False
