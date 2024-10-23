import os
import xarray as xr
import pandas as pd


def read_and_store_dimensions(file):
    """  """
    with xr.open_dataset(file) as ds:
        dims = dict(ds.sizes)
        dims["filename"] = os.path.basename(file)
        dims["filepath"] = file
        return pd.DataFrame(dims, index=[0])