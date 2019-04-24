import pytest
from ie_pandas import DataFrame


def input_type_test():
    """This test checks to make sure only dictionaries are allowed"""
    input_list = [1, 2, 3]
    with pytest.raises(ValueError):
        assert DataFrame(input_list)


def input_value_test():
    """ This test checks to make sure that values other than lists and 
    numpy arrays are not allowed"""
    input_dic = {"a": 2, "b": 3}
    with pytest.raises(ValueError):
        assert DataFrame(input_dic)


def input_length_test():
    """This test checks to make sure columns are of the same length"""
    input_dic = {"a": [1, 2, 3], "b": [3, 4, 5, 6]}
    with pytest.raises(ValueError):
        assert DataFrame(input_dic)


def input_same_value_test():
    """This test checks to make sure values in each columns are of the same type"""
    input_dic = {"a": [1, 2, 3, "g"], "b": [3, 4, 5, 6]}
    with pytest.raises(ValueError):
        assert DataFrame(input_dic)
        

    

        

