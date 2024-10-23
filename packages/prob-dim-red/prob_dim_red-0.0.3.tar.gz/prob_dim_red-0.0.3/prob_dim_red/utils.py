# Copyright 2024, INRAE, France, François Victor <francois.victor@inrae.fr>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""file containing functions and classes that may be useful"""
from dataclasses import dataclass
from typing import NamedTuple
from fractions import Fraction

import numpy as np
import numpy.typing as npt


# pylint:disable=unexpected-keyword-arg
class _VectorizedArray(NamedTuple):
    """A class for vectorized matrices.

    This class is used to instantiate vectorized array
    and to store which index varies the fastest in memory,
    respectively the former and latter in Fortran-style
    and C-style.

    Attributes
    ----------
    order_c : bool
        Flag indicating if the array is in C-contiguous order.
    order_f : bool
        Flag indicating if the array is in Fortran-contiguous order.
    vec : np.ndarray
        The vectorized array.
    """

    order_c: bool
    order_f: bool
    vec: np.ndarray


class _NotVectorizable(Exception):
    """
    Custom exception raised when an array cannot be vectorized.
    """


def _vecto(A):
    """
    Vectorize a 2D array and return its order information.

    This function takes a 2D array and checks if it can be vectorized by
    reshaping it into a 1D array using strides. If the array is not
    vectorizable, it raises a `_NotVectorizable` exception.

    Parameters
    ----------
    A : np.ndarray
        A 2D array to be vectorized.

    Returns
    -------
    _VectorizedArray
        A named tuple containing the vectorized array and its order information.

    Raises
    ------
    _NotVectorizable
        If the array cannot be vectorized.
    """
    assert len(A.shape) == 2
    n1, n2 = A.shape
    s1, s2 = A.strides
    if n1 == 1:
        s1 = s2
    if n2 == 1:
        s2 = s1
    is_order_c = s1 >= s2
    is_order_f = s1 <= s2
    if is_order_c:
        if n1 > 1 and s2 * n2 != s1:
            raise _NotVectorizable
        vec = np.lib.stride_tricks.as_strided(A, shape=(n1 * n2,), strides=(s2,))
    else:
        if n2 > 1 and s1 * n1 != s2:
            raise _NotVectorizable
        vec = np.lib.stride_tricks.as_strided(A, shape=(n1 * n2,), strides=(s1,))
    return _VectorizedArray(is_order_c, is_order_f, vec)


def data_load(data: npt.ArrayLike) -> npt.NDArray[np.float64]:
    """
    Load data from an array-like object and return a NumPy array.

    Parameters
    ----------
    data : array_like
        The input data to be converted to a NumPy array.

    Returns
    -------
    numpy.ndarray
        A NumPy array representing the input data.
    """
    return np.asarray(data)


def trace_matmul(
    mat_a: npt.ArrayLike, mat_b: npt.ArrayLike, sym: bool = False
) -> np.number:
    """
    Computes and returns the trace of the product of input matrices.

    Parameters
    ----------
    mat_a : array_like
        The array_like given as the first operand of the matrix multiplication.

    mat_b : array_like
        The array_like given as the second operand of the matrix multiplication.

    sym : bool
        Use optimized method if at least one matrix is symmetric.
        Warning: No symmetry check is performed, if both matrix are not symmetric,
        result is unpredictable

    Returns
    -------
    numpy.ndarray
        A NumPy array of the trace of the matrix product (scalar).
    """

    mat_a = np.asarray(mat_a)

    mat_b = np.asarray(mat_b)

    a_rows, a_cols = mat_a.shape
    b_rows, b_cols = mat_b.shape

    assert (a_cols == b_rows) and (a_rows == b_cols)

    try:
        vec_a = _vecto(mat_a)
        vec_b = _vecto(mat_b)

        if (
            (vec_a.order_c and vec_b.order_f)
            or (vec_a.order_f and vec_b.order_c)
            or sym
        ):
            return vec_a.vec @ vec_b.vec

    except _NotVectorizable:
        pass

    if sym and not (
        (mat_a.strides[0] < mat_a.strides[1]) ^ (mat_b.strides[0] < mat_b.strides[1])
    ):
        return np.einsum("ij,ij->", mat_a, mat_b)

    return np.einsum("ij,ji->", mat_a, mat_b)


def positive_part(x: npt.ArrayLike) -> npt.NDArray[np.float64]:
    """
    Compute the positive part of an array element-wise.

    This function returns an array where each element is the maximum of the input
    element and zero, effectively replacing all negative values with zero.

    Parameters
    ----------
    x : array-like
        Input array or scalar to compute the positive part.

    Returns
    -------
    ndarray
        An array with the same shape as `x`, where each element is the positive
        part of the corresponding element in `x`.
    """
    return np.maximum(x, 0)


def log_with_zeros(x: npt.ArrayLike) -> npt.NDArray[np.float64]:
    """
    Compute the natural logarithm of an array, treating zeros safely.

    This function computes the natural logarithm of each element in the input array.
    For elements equal to zero, it returns positive infinity instead of `-inf`, and
    for negative elements, the function asserts an error as the logarithm is undefined.

    Parameters
    ----------
    x : array-like
        Input array or scalar for which the logarithm is computed. All elements must be
        non-negative.

    Returns
    -------
    ndarray
        An array with the same shape as `x`, where each element is the natural logarithm
        of the corresponding element in `x`. Elements that are zero are mapped to positive infinity.
    """
    assert (np.asarray(x) >= 0).all()

    return np.log(x, out=np.full_like(x, np.inf), where=x > 0)


@dataclass
class FractionOrInf:
    """
    Attributes
    ----------
    value
    """

    value: Fraction | np.float64

    def __init__(self, value: Fraction | np.float64):
        if isinstance(value, Fraction):
            self.value = value
            return
        if np.isinf(value):
            self.value = value
            return
        self.value = Fraction(value)

    def __add__(self, oth: "FractionOrInf"):
        if isinstance(self.value, Fraction) and isinstance(oth.value, Fraction):
            return FractionOrInf(self.value + oth.value)
        return FractionOrInf(np.float64(self.value) + np.float64(oth.value))

    def __float__(self):
        return float(self.value)
