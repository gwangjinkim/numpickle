
# numpickle

Faster loading of pandas data frames by saving them as numpy arrays and pickling their meta info (row+column names, column dtype info).

The bigger the data frame, the bigger the gain of speed when reading compared to loading a text file.
(E.g., a several GB RAM-consuming matrix took minutes to read-in using normal `pd.read_csv()`, but took only seconds to load when using `numpickle.load_numpickle()`).
`all_numeric=True` accelerates loading by ~ 7 times.

Also mentioned in my [medium article](https://gwang-jin-kim.medium.com/faster-loading-and-saving-of-pandas-data-frames-using-numpickle-numpy-and-pickle-d15870519529)

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






####################################
# data frames with numeric-only values
###################################

# If you have a data frame with only numeric values, put all_numeric=True .
# Then dtypes is set to None and the loading will be slightly faster.
df = pd.DataFrame([[1, 2], [3, 4]])
df.columns = ["A", "B"]
df.index = ["row1", "row2"]

df
#       A  B
# row1  1  2
# row2  3  4

df.dtypes
# A     int64
# B     int64
# dtype: object

# save numeric-only data frame
npl.save_numpickle(df, "/home/user/test.npy", all_numeric=True)
# load numeric-only data frame (it recognizes automatically that it is numeric only
# because dtypes=None or not existent in pickle file
df_ = npl.load_numpickle("/home/user/test.npy")


###################################
# save a csv or tab file as numpickle file(s) and delete original files
###################################
npl.save_file_as_numpickle(fpath, sep="\t", ending=".tab", all_numeric=True, deletep=True)
# the data are read by pd.read_csv(), additional arguments for the reading process can be given
# into the argument list, they will be forwarded to pd.read_csv() by *args, **kwargs
# for the output file name, the `ending` is replaced by ".npy" and ".npy.pckl".
# So choose the separator and ending accordingly when file is a csv file (sep=",", ending=".csv").
```


