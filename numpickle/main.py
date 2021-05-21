import pandas as pd
import numpy as np
import pickle
import os


def save_numpickle(df, outfpath, all_numeric=False):
    arr, colnames, rownames = df.to_numpy(), df.columns, df.index
    np.save(arr=arr, file=outfpath)
    pickle.dump({'colnames': colnames, 'rownames': rownames, 'dtypes': None if all_numeric else df.dtypes}, 
                open(outfpath + ".pckl", "wb"))

def load_numpickle(fpath):
    df = pd.DataFrame(np.load(fpath, allow_pickle=True))
    with open(fpath + ".pckl", "rb") as fin:
        meta = pickle.load(fin)
    # if no 'types' present, assuming all_numeric
    df.index, df.columns, dtypes = meta['rownames'], meta['colnames'], meta.get('dtypes', None)
    if dtypes is not None:
        df = df.astype(dtypes)
    return df

def save_file_as_numpickle(fpath, sep="\t", ending=".tab", all_numeric=False, deletep=False, *args, **kwargs):
    df = pd.read_csv(fpath, sep=sep, *args, **kwargs)
    save_numpickle(df, fpath.replace(ending, ".npy"), all_numeric=all_numeric)
    if deletep:
        os.remove(fpath)


