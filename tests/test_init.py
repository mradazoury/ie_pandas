import pytest
import numpy as np
from ie_pandas.DataFrame import DataFrame


def test_input_type():
    """This test checks to make sure only dictionaries are allowed"""
    input_list = [1, 2, 3]
    with pytest.raises(ValueError):
        assert DataFrame(input_list)


def test_input_value():
    """ This test checks to make sure that values other than lists and 
    numpy arrays are not allowed"""
    input_dic = {"a": 2, "b": 3}
    with pytest.raises(ValueError):
        assert DataFrame(input_dic)


def test_input_length():
    """This test checks to make sure columns are of the same length"""
    input_dic = {"a": [1, 2, 3], "b": [3, 4, 5, 6]}
    with pytest.raises(ValueError):
        assert DataFrame(input_dic)


def test_input_same_value():
    """This test checks to make sure values in each columns are of the same type"""
    input_dic = {"a": [1, 2, 3, "g"], "b": [3, 4, 5, 6]}
    with pytest.raises(ValueError):
        assert DataFrame(input_dic)
