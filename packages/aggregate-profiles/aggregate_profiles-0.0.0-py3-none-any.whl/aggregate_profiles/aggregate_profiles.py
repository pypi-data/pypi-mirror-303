# module of profiles aggregation
# this module allows the aggregation of oceanographic profiles

import pandas as pd
import xarray as xr
import warnings
from read_and_write import read_and_store_dimensions
from multiprocess import exec_mlproc_function
from utils import open_and_expand

def main(files, prof_axis):
    
    # creation of dataframes containing all files informations about dimensions and locations
    df_list = list(map(read_and_store_dimensions, files))
    
    # concatenate dataframes to summarize informations about files and dimensions
    df_dims = pd.concat(list(df_list)).reset_index().drop("index", axis=1)
    
    # if prof_axis not in files dimensions trigger warning 
    if prof_axis not in df_dims.columns.names:
        warnings.warn("Warning : concatenation axis is not in files dimensions, concatenation alog this new axis ")
        
    # check if any dimension is not shared by all files 
    nansum = df_dims[df_dims.columns.difference(['filepath', 'filename'])].isna().sum()
    undesirable_dimensions = nansum[nansum !=0].to_dict()

    # if any dim not shared by all, remove from shared dims and max levels : 
    cols_to_exclude = list(undesirable_dimensions.keys())
    [cols_to_exclude.append(x) for x in ['filepath', 'filename']]
    
    # compute max_n_levels : sizes max of each dimension shared by all files 
    max_n_levels = df_dims[df_dims.columns.difference(cols_to_exclude)].max().to_dict()
    
    res_computed = exec_mlproc_function(files, open_and_expand, max_n_levels, prof_axis, undesirable_dimensions)
    aggregated_dataset = xr.concat(res_computed, dim=prof_axis)
    
    return aggregated_dataset

if __name__ == "__main__":
    # Example usage (assuming files and prof_axis are defined)
    files = ['/runtime/data/6901580/profiles/BD6901580_032.nc', '/runtime/data/6901580/profiles/D6901580_050.nc']  # Replace with actual file paths
    prof_axis = 'N_PROF'  # Replace with the desired profile axis
    aggregated_data = main(files, prof_axis)
    print(aggregated_data)