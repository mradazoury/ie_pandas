import pytest
from ie-pandas import DataFrame

@pytest.mark.parametrize("df , expected",[({'name':['Georges','Alexandre','Kelly'],
                                           'Family': ['Koury', 'Trump', 'McKinsey'],
                                           'age': [25, 26, 30]},
                                          [25, 26, 30])  
                                        ,({'name':['Georges','Alexandre','Kelly'],
                                           'Family': ['Koury', 'Trump', 'McKinsey'],
                                           'age': [25, 26, 30]}
                                          ,[['Koury', 'Trump', 'McKinsey'],[25, 26, 30]])])

def test_get_item(df, expected):
    df = DataFrame(df)
    assert df == expected