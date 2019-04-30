import numpy as np


class DataFrame:
    def __init__(self, df):
        df = df.copy()
        # checking the type to make sure it is a dicitonary
        if type(df) != dict:
            raise ValueError("Wrong input type, Only dictionaries are acceptable")

            # Only letting list and numpy array to be set as values in the dictionary
        for i in df.values():
            if isinstance(i, (list, np.ndarray)):
                pass
            else:
                raise ValueError(
                    " Only dictionaries of list or Numpy array are acccepted"
                )

        l = []
        for i in df.values():
            l.append(len(i))

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

    def __getitem__(self, colname):
        """ This function returns the values of the called column"""
        if isinstance(colname, str):
            if colname in self.keys:
                return np.array(self.df[colname])
            else:
                raise IndexError(
                    "Column Name does not exist, Please enter a correct column Name"
                )
        elif isinstance(colname, (list, tuple)):
            for y in colname:
                if y not in self.keys:
                    raise IndexError(
                        "Column Name does not exist, Please enter a correct column Name"
                    )
                else:
                    return np.array([np.array(self.df[x]) for x in colname])

    def __setitem__(self, colname, value):
        """ This function sets the values of the called column"""
        if isinstance(value, (list, np.ndarray)):
            pass
        else:
            raise ValueError(" Only list or Numpy array are acccepted")
        if len(value) == len(self.values[0]):
            pass
        else:
            raise ValueError("Length of values does not match length of index")
        if all(
            isinstance(
                x, (int, float, str, bool, np.int_, np.float_, np.chararray, np.bool_)
            )
            for x in value
        ):
            pass
        else:
            raise ValueError(
                "Wrong data type, Only integer, float, boolean and string are accepted"
            )

        l = []
        for i in value:
            l.append(type(i))
        if len(set(l)) > 1:
            raise ValueError("All the values in a column should be of the same type")
        else:
            self.df[colname] = value

    def __repr__(self):
        returnString = (
            str(list(self.df.keys()))
            + "\n"
            + str(np.transpose(np.array(list(self.df.values()), dtype="O")))
        )
        return returnString


    def __add__(self,other):
        """This dunder function adds the number after a + sign to every numerical column"""
        for k in self.keys:
            if np.issubdtype(np.array(self.df[k]).dtype, np.number):
                if isinstance(self.df[k] , list):
                    self.df[k] = list(np.array(self.df[k]) + other)
                else:
                    self.df[k] = self.df[k] + other
                    
    def __sub__(self,other):
        """This dunder function substracts the number after a + sign to every numerical column"""
        for k in self.keys:
            if np.issubdtype(np.array(self.df[k]).dtype, np.number):
                if isinstance(self.df[k] , list):
                    self.df[k] = list(np.array(self.df[k]) - other)
                else:
                    self.df[k] = self.df[k] - other   
                    
    def __mul__(self,other):
        """This dunder function multiplies the number after a + sign to every numerical column"""
        for k in self.keys:
            if np.issubdtype(np.array(self.df[k]).dtype, np.number):
                if isinstance(self.df[k] , list):
                    self.df[k] = list(np.array(self.df[k]) * other)
                else:
                    self.df[k] = self.df[k] * other 
    
    def __truediv__(self,other):
        """This dunder function divides the number after a + sign to every numerical column"""
        for k in self.keys:
            if np.issubdtype(np.array(self.df[k]).dtype, np.number):
                if isinstance(self.df[k] , list):
                    self.df[k] = list(np.array(self.df[k]) / other)
                else:
                    self.df[k] = self.df[k] / other    

    def colnames(self):
        """ This method returns the name of columns"""
        l = []
        for k in self.keys:
            l.append(k)
        return l

    def get_row(self, index_start, index_end = None):
        """ This method returns the cited rows"""
        d = []
        if index_end == None:
            for k in self.keys:
                d.append((self.df[k])[index_start])
        else:
            for k in self.keys:
                d.append((self.df[k])[index_start:index_end + 1])
            d = list(map(list, zip(*d)))

        return d

    # mathematical functions
     def sum(self):  ### fix it to be just for numerical  -- done  --- works without ie_
        """ This method returns a dictionary including the sum of all columns"""
        d = []
        for k in self.keys:
            if np.issubdtype(np.array(self.df[k]).dtype, np.number):
                d.append(sum(self.df[k]))
        return d

    def median(self):
        """ This method returns a dictionary including the median of all columns"""
        d = []
        for k in self.keys:
            if np.issubdtype(np.array(self.df[k]).dtype, np.number):
                d.append(np.median(self.df[k]))
        return d

    def min(self):
        """ This method returns a dictionary including the min of all columns"""
        d = []
        for k in self.keys:
            if np.issubdtype(np.array(self.df[k]).dtype, np.number):
                d.append(np.min(self.df[k]))
        return d

    def max(self):
        """ This method returns a dictionary including the max of all columns"""
        d = []
        for k in self.keys:
            if np.issubdtype(np.array(self.df[k]).dtype, np.number):
                d.append(np.max(self.df[k]))
        return d

    def shape(self):
        """This method returns a tuple of the number of rows and number of columns"""
        
        row = len(self.values[0])
        col = len(self.keys)
        l = (row , col)
        return l
    
    def dtypes(self):
        """This method returns the types of each of the columns in the DataFrame"""
        s = ""
        for k in self.keys:
            s =  s + "{0}: {1}, ".format(k, type(self.df[k][0]).__name__ )
        return s[:-2] 