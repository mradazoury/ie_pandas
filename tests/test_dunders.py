import pytest
import numpy as np
from ie_pandas.DataFrame import DataFrame

_dic1 = {
    "name": ["Georges", "Alexandre", "Kelly"],
    "Family": ["Koury", "Trump", "McKinsey"],
    "age": [25, 26, 30],
}

_df = DataFrame(_dic1)

_dic2 = {"a": [3, 4, 5, 6], 1: [3, 4, 5, 6]}

_df2 = DataFrame(_dic2)

_dic3 = {"list" : [10 ,11 ,12, 13] , "numpy" : np.array([7,8,9,10]) , "str" : ['a' ,'b' ,'c' ,'d']}

_df3 = DataFrame(_dic3)

@pytest.mark.parametrize(
    "expected, colnames",
    [
        (np.array([25, 26, 30]), ("age")),
        (
            np.array(
                [np.array(["Koury", "Trump", "McKinsey"]), np.array([25, 26, 30])]
            ),
            ("Family", "age"),
        ),
    ],
)
def test_get_item(expected, colnames):
    """Testing two cases, one where only one column is called and another one where two columns are called"""
    assert np.unique(_df[colnames] == expected) == True


def test_get_item_error():
    """Testing a case where the column called does not exist"""
    with pytest.raises(IndexError):
        assert _df[("Country")]


def test_set_item():
    """Testing that __setitem__ assigns a new column"""
    _df2["New_column"] = ["1", "2", "3", "4"]
    assert np.unique(_df2["New_column"] == np.array(["1", "2", "3", "4"])) == True


@pytest.mark.parametrize(
    "new_column",
    [["1", "2", "3"], [1, 2, 3, "a"], "a string", [None, None, None, None]],
)
def test_set_item_errors(new_column):
    """Testing cases where the new column, is not of the same length, is not a list or tuple 
  , has values of different types, and has values different then string number and boolean"""
    with pytest.raises(ValueError):
        _df2["New_column"] = new_column


def test_repr():
    """ Testing that the representation is how we designed it"""
    assert (
        repr(_df)
        == "['name', 'Family', 'age']\n[['Georges' 'Koury' 25]\n ['Alexandre' 'Trump' 26]\n ['Kelly' 'McKinsey' 30]]"
    )


@pytest.mark.parametrize(
    "df,expected", [(_df, ["name", "Family", "age"]), (_df2, ["a", 1, "New_column"])]
)
def test_col_name(df, expected):
    """ Testing that colnames returns all the column names"""
    assert df.colnames() == expected

@pytest.mark.parametrize(
    "start,end,expected", [(0 ,1 , [["Georges", "Koury", 25],["Alexandre","Trump" ,26]]), (2,None ,["Kelly", "McKinsey", 30])]
)
def test_get_row(start , end , expected):
  """Testing that get_row() gives back the rows inputed"""
  if end == None:
    assert _df.get_row(start) == expected
  else:
    assert _df.get_row(start,end) == expected

def test_add_():
  """Testing that the + sign will add the next number to all the numerical columns"""
  test = _df3['list']
  _df3 + 5
  assert np.unique(_df3['list'] == test + 5 ) == True

def test_sub_():
  """Testing that the - sign will substract the next number from all the numerical columns"""
  test = _df3['list']
  _df3 - 5
  assert np.unique(_df3['list'] == test - 5 ) == True

def test_mul_():
  """Testing that the * sign will multiply the next number with all the numerical columns"""
  test = _df3['list'] 
  _df3 * 5
  assert np.unique(_df3['list' ]== test * 5 ) == True

def test_div_():
  """Testing that the / sign will divide all the numerical columns by the next number"""
  test = _df3['list']
  _df3 / 5
  assert np.unique(_df3['list'] == test / 5 ) == True

def test_shape():
  """Testing that the shape function returns the shape of the data frame (row , col)"""
  assert _df.shape() == (3,3)

def dtypes():
  """ Testing that the function dtypes returns the type of each of the columns"""
  assert _df.dtypes() == 'name: str, Family: str, age: int'

