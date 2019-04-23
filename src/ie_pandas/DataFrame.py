class dataframe:
    def __init__(self, df):

        # checking the type to make sure it is a dicitonary
        if type(df) != dict:
            raise ValueError("Wrong input type, Only dictionaries are acceptable")

        else:
            l = []
            for i in df.values():
                l.append(len(i))

        # Only letting list and numpy array to be set as values in the dictionary
        for i in df.values():
            if isinstance(i, (list, np.ndarray)):
                pass
            else:
                raise ValueError(
                    " Only dictionaries of list or Numpy array are acccepted"
                )

        # making sure that all columns are of same length
        if len(set(l)) > 1:
            raise ValueError("Columns with unequal length are not accepted")

        else:
            for i in df.values():
                if all(
                    isinstance(
                        x,
                        (
                            int,
                            float,
                            str,
                            bool,
                            np.int_,
                            np.float_,
                            np.chararray,
                            np.bool_,
                        ),
                    )
                    for x in i
                ):
                    pass
                else:
                    raise ValueError(
                        "Wrong data type, Only integer, float, boolean and string are accepted"
                    )
        # Making sure that all values in a column are of the same type
        for i in df.values():
            l = []
            for value in i:
                l.append(type(value))

            if len(set(l)) > 1:
                raise ValueError("All the values in a column should be the same")

            else:
                self.df = df
                self.keys = df.keys()
                l = []
                for v in df.values():
                    l.append(v)
                self.values = l