
Install
=======

``
pip install numpickle as npl
``

Usage
=====

``
import pandas as pd

# example data frame with numeric content
df = pd.DataFrame([[1, 2], [3, 4]])
df.columns = ["A", "B"]
df.index = ["row1", "row2"]

df
#       A  B
# row1  1  2
# row2  3  4

# example data frame with non-numeric columns
df1 = pd.DataFrame([[1, 2,'a'], [3, 4, 'b']])
df1.columns = ["A", "B", "C"]
df1.index = ["row1", "row2"]

# save data frame as numpy array and pickle the row and column names
npl.save_numpickle(df, "/home/user/test.npy")
# the pickled names of column and rows are saved into "~/.test.npy.pckl"

# load data frame from numpy array and its corresponding pickle file
df_ = npl.load_numpickle("/home/user/test.npy")



# save data frame as numpy array and pickle the row and column names
npl.save_numpickle(df1, "/home/user/test1.npy")
# the pickled names of column and rows are saved into "/home/user/.test.npy.pckl"

# load data frame from numpy array and its corresponding pickle file
df1_ = npl.load_numpickle("/home/user/test1.npy")
``


