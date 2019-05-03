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
        
'''tests for mathematical functions sum, median, min and max'''
_math_dic = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': ['a', 'b', 'c', 'd', 'e']}
_df = DataFrame(_math_dic)
        
def test_sum():
    ''' Test and compare the results from the sum function against the expected results'''
    result = _df.sum()
    expected = [15 ,40]
    assert result == expected
    print("The results from the test max the expected results", expected)

def test_median():
        ''' Test and compare the results from the median function against the expected results'''
        result = _df.median()
        expected = [ 3 ,8]
        assert result == expected
        print("The results from the test match the expected results", expected)
        
def test_min():
        ''' Test and compare the results from the min function against the expected results'''
        result = _df.min()
        expected = [ 1 , 6]
        assert result == expected
        print("The results from the test match the expected results", expected)
        
def test_max():
        ''' Test and compare the results from the max function against the expected results'''
        result = _df.max()
        expected = [ 5 , 10 ]
        assert result == expected
        print("The results from the test match the expected results", expected)
