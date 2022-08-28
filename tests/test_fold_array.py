import pytest
from solutions.fold_array import fold_array

def test_fold_array():
   a = fold_array([1,2,3,4],2)
   assert a == [10]