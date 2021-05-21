
# numpickle

Faster loading of pandas data frames by saving them as numpy arrays and pickling their meta info (row+column names, column dtype info).

## Install

```pip install numpickle```

## Usage

```
import pandas as pd
import numpickle as npl


# create example data frame with non-numeric and numeric columns
df = pd.DataFrame([[1, 2,'a'], [3, 4, 'b']])
df.columns = ["A", "B", "C"]
df.index = ["row1", "row2"]

df
#       A  B  C
# row1  1  2  a
# row2  3  4  b

df.dtypes
# A     int64
# B     int64
# C    object
# dtype: object




# save data frame as numpy array and pickle row and column names
# into helper pickle file "/home/user/test.npy.pckl"
npl.save_numpickle(df, "/home/user/test.npy")

# load the saved data
df_ = npl.load_numpickle("/home/user/test.npy")

df_
#       A  B  C
# row1  1  2  a
# row2  3  4  b


df_.dtypes
# A     int64
# B     int64
# C    object
# dtype: object

all(df == df_)
# True

```


