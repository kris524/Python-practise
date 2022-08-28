import pytest
from solutions.fold_array import fold_array


def test_fold_array():
    a = fold_array([1, 2, 3, 4], 2)
    assert a == [10]


def test_fold_array_odd():
    a = fold_array([1, 2, 3, 4, 5], 2)
    assert a == [6, 6, 3]

