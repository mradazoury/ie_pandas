import pytest
import numpy as np
from ie_pandas.DataFrame import DataFrame

dic1 = {
                "name": ["Georges", "Alexandre", "Kelly"],
                "Family": ["Koury", "Trump", "McKinsey"],
                "age": [25, 26, 30],
            }
@pytest.mark.parametrize(
    "df, expected, colnames",
    [
        (
            dic1,
            [[25, 26, 30]],
            ("age"),
        ),
        (
            dic1,
            [["Koury", "Trump", "McKinsey"], [25, 26, 30]],
            ("Family", "age"),
        ),
    ],
)
def test_get_item(df, expected, colnames):
    df = DataFrame(df)
    assert df[colnames] == expected

# def test_get_item_error():
#     df = DataFrame(dic1)
#     with pytest.raises(ValueError):
#     assert DataFrame(input_dic)
