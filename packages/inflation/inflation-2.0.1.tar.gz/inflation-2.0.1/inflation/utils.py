"""
This file contains auxiliary functions of general purpose

@authors: Emanuel-Cristian Boghiu, Elie Wolfe and Alejandro Pozas-Kerstjens
"""
from __future__ import print_function
import numpy as np
import scipy.sparse as sps
from itertools import chain
from typing import Iterable, Union, List, Tuple, Dict
from sys import stderr
from operator import itemgetter


def flatten(nested):
    """Keeps flattening a nested lists of lists until  the
    first element of the resulting list is not a list.
    """
    if isinstance(nested, np.ndarray):
        return nested.ravel().tolist()
    else:
        while isinstance(nested[0], Iterable):
            nested = list(chain.from_iterable(nested))
        return nested

def format_permutations(array: Union[
    np.ndarray,
    List[List[int]],
    List[Tuple[int,...]],
    Tuple[Tuple[int,...],...],
    Tuple[List[int],...],
]) -> np.ndarray:
    """Permutations of inflation indices must leave the integers 0,
    corresponding to sources not being measured by the operator, invariant.
    In order to achieve this, this function shifts a permutation of sources
    by 1 and prepends it with the integer 0.

    Parameters
    ----------
    array : numpy.ndarray
        2-d array where each row is a permutations.

    Returns
    -------
    numpy.ndarray
        The processed list of permutations.
    """
    source_permutation = np.asarray(array) + 1
    return np.pad(source_permutation, ((0, 0), (1, 0)))

def clean_coefficients(cert: Dict[str, float],
                       chop_tol: float = 1e-10,
                       round_decimals: int = 3) -> Dict:
    """Clean the list of coefficients in a certificate.

    Parameters
    ----------
    cert : Dict[str, float]
      A dictionary containing as keys the monomials associated to the elements
      of the certificate and as values the corresponding coefficients.
    chop_tol : float, optional
      Coefficients in the dual certificate smaller in absolute value are
      set to zero. Defaults to ``1e-10``.
    round_decimals : int, optional
      Coefficients that are not set to zero are rounded to the number
      of decimals specified. Defaults to ``3``.

    Returns
    -------
    np.ndarray
      The cleaned-up coefficients.
    """
    if not cert:
        return cert
    chop_tol = np.abs(chop_tol)
    coeffs = np.asarray(list(cert.values()))
    if chop_tol > 0:
        # Try to take the smallest nonzero one and make it 1, when possible
        normalising_factor = np.min(np.abs(coeffs[np.abs(coeffs) > chop_tol]))
    else:
        # Take the largest nonzero one and make it 1
        normalising_factor = np.max(np.abs(coeffs[np.abs(coeffs) > chop_tol]))
    coeffs /= normalising_factor
    # Set to zero very small coefficients
    coeffs[np.abs(coeffs) <= chop_tol] = 0
    # Round
    coeffs = np.round(coeffs, decimals=round_decimals)
    return dict(zip(cert.keys(), coeffs.flat))

def eprint(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

def partsextractor(thing_to_take_parts_of, indices) -> Tuple[int,...]:
    if hasattr(indices, '__iter__'):
        if len(indices) == 0:
            return tuple()
        elif len(indices) == 1:
            return (itemgetter(*indices)(thing_to_take_parts_of),)
        else:
            return itemgetter(*indices)(thing_to_take_parts_of)
    else:
        return itemgetter(indices)(thing_to_take_parts_of)


def expand_sparse_vec(sparse_vec: sps.coo_array,
                      conversion_style: str = "eq") -> sps.coo_array:
    """Expand a one-dimensional sparse matrix to its full form. Used to expand
    the solver arguments known_vars, lower_bounds, and upper_bounds."""
    assert conversion_style in {"eq", "lb", "ub"}, \
        "Conversion style must be `lb`, `ub`, or `eq`."
    nof_rows = sparse_vec.nnz
    nof_cols = sparse_vec.shape[1]
    if conversion_style == "eq":
        # Data values do not appear in '1' monomial column
        row = np.arange(nof_rows)
        col = sparse_vec.col
        data = np.ones(nof_rows)
    else:
        # Data values appear in '1' monomial column
        # Upper bound format: x <= a -> a - x >= 0
        row = np.repeat(np.arange(nof_rows), 2)
        col = np.vstack((
            sparse_vec.col,
            np.zeros(nof_rows)  # Assumes '1' monomial is first column
        )).T.ravel()
        data = np.vstack((
            -np.ones(nof_rows),
            sparse_vec.data,
        )).T.ravel()
    if conversion_style == "lb":
        # Lower bound format: x >= a -> x - a >= 0
        data = -data
    return sps.coo_array((data, (row, col)), shape=(nof_rows, nof_cols))


def vstack(blocks: tuple, format: str = 'coo') -> sps.coo_array:
    """Stack sparse matrices in coo_array form more efficiently."""
    non_empty = tuple(mat for mat in blocks if mat.shape[0])
    nof_blocks = len(non_empty)
    if nof_blocks > 1:
        if all(isinstance(block, sps.coo_array) for block in blocks):
            # mat_row = blocks[0].row
            # (row_count, _) = blocks[0].shape
            # for block in blocks[1:]:
            #     mat_row = np.concatenate((mat_row,
            #                               block.row + row_count))
            nof_rows = 0
            nof_cols = 0
            adjusted_rows = []
            for block in blocks:
                adjusted_rows.append(block.row + nof_rows)
                (block_len, block_wid) = block.shape
                nof_rows += block_len
                nof_cols = max(nof_cols, block_wid)
            mat_row = np.hstack(adjusted_rows)
            mat_col = np.hstack(tuple(block.col for block in blocks))
            mat_data = np.hstack(tuple(block.data for block in blocks))
            return sps.coo_array((mat_data, (mat_row, mat_col)),
                                  shape=(nof_rows, nof_cols)).asformat(format)
        else:
            return sps.vstack(blocks, format)
    elif nof_blocks == 1:
        return non_empty[0]
    else:
        return sps.coo_array([])

def perm_combiner(old_perms: np.ndarray, new_perms: np.ndarray) -> np.ndarray:
    combined = np.take(old_perms, new_perms, axis=1)
    # combined = old_perms.T[new_perms.T]
    new_shape = ((-1, new_perms.shape[1]))
    return combined.reshape(new_shape)
