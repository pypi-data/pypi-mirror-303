

import numpy as np
import xarray as xr
from typing import Any, Dict, List, Optional

def decode_byte_strings(data_array: xr.DataArray) -> xr.DataArray:
    """Decode byte strings in a data array and convert NaN values.

    Args:
        data_array (xr.DataArray): The input data array that may contain byte strings and NaN values.

    Returns:
        xr.DataArray: A new data array with decoded strings and NaN converted to 'nan'.
    """
    
    def decode_value(value: Any) -> Any:
        if isinstance(value, bytes):
            try:
                return value.decode('utf-8')
            except UnicodeDecodeError:
                return value  # Return original if decoding fails
        if isinstance(value, float) and np.isnan(value):
            return 'nan'
        return value
    
    vectorized_decode = np.vectorize(decode_value)
    
    return xr.apply_ufunc(vectorized_decode, data_array, keep_attrs=True)



# ---------------------------------------------------------



def compute_n_missing_lines(ds: xr.Dataset, max_n_levels: Dict[str, int]) -> Dict[str, int]:
    """Compute the number of missing lines for each dimension in the dataset.

    Args:
        ds (xr.Dataset): The xarray dataset to analyze.
        max_n_levels (Dict[str, int]): A dictionary mapping dimension names to their maximum levels.

    Returns:
        Dict[str, int]: A dictionary containing the number of missing lines for each dimension.
    """
    
    keys = list(dict(ds.sizes).keys())
    max_levels = []
    ds_levels = []

    for k in keys:
        max_levels.append(max_n_levels[k])
        ds_levels.append(ds.sizes[k])

    diff = np.array(max_levels)-np.array(ds_levels)
    
    return dict(zip(keys, diff))


# ---------------------------------------------------------



def find_variables_with_dimension(ds: xr.Dataset, dim_name: str) -> List[str]:
    """
    Find variables in an xarray dataset that are associated with a specific dimension.

    Parameters:
    ds (xarray.Dataset): The xarray dataset.
    dim_name (str): The dimension name to check.

    Returns:
    List[str]: A list of variable names that have the specified dimension.
    """
    variables_with_dim = [var for var in ds.data_vars if dim_name in ds[var].dims]
    return variables_with_dim



# ---------------------------------------------------------


def expand_dimensions(
    ds: xr.Dataset, 
    dim_sizes: Dict[str, int], 
    z_axis: str, 
    undesirable_dimensions: Optional[List[str]] = None
) -> xr.Dataset:
    """expand dimensions from a dataset along those specified in .

    Parameters:
        ds_name (str): The name of the dataset to open.
        dim_sizes (Dict[str, int]): Dimension size desired for each dimension.
        z_axis (str): The dimension along which to concatenate.
        undesirable_dimensions (Optional[List[str]]): Dimensions to exclude from the dataset.

    Returns:
        xr.Dataset: A new dataset with the concatenated dimensions and padding.
    """
    
    # Remove variables associated with undesirable dimensions
    if undesirable_dimensions:
        for dim in undesirable_dimensions:
            ds = ds.drop_vars(find_variables_with_dimension(ds, dim), errors='raise')
    
    # Compute number of missing lines
    nb_missing_lines = compute_n_missing_lines(ds, dim_sizes)
    # Set the missing lines for the z-axis to 0
    nb_missing_lines[z_axis] = 0

    # Instantiate a new empty dataset
    new_ds = xr.Dataset()
    for dim, dim_size in ds.sizes.items():
        if nb_missing_lines[dim] == 0:
            new_ds[dim] = xr.DataArray(data=np.arange(dim_size), dims=dim)
        else:
            new_ds[dim] = xr.DataArray(data=np.arange(dim_sizes[dim]), dims=dim)

    # Extend dimensions and pad variables
    for var in ds.data_vars:
        # patch test type of vars:
        try:
            decoded_var = decode_byte_strings(ds[var])
        except ValueError:
            decoded_var = ds[var]
        
        # creating dict for padding 
        if not ds[var].sizes:
            padding_dict = {z_axis: (0, 1)}
        else :
            padding_dict = {}
            for vardim in ds[var].sizes:
                padding_dict[vardim] = (0, nb_missing_lines[vardim])
        
        # pad each variable to match new dataset dimensions    
        padded = decoded_var.pad(pad_width=padding_dict, constant_values=None)
            
        if padded.dtype == "object" :
            new_ds[var] = padded.astype(str)
        else :
            new_ds[var] = padded

    # drop initial variables 
    new_ds = new_ds.drop_vars(list(ds.sizes.keys()))

    # copy attributes from old dataset
    new_ds.attrs = ds.attrs
    
    return new_ds


# ---------------------------------------------------------

def open_and_expand(file: str, dim_sizes: Dict[str, int], nontaken_axis: str, undesirable_dimensions: Dict[str, Any]) -> xr.Dataset:
    """Open an xarray dataset and expand its dimensions.

    Args:
        file (str): The path to the file to open.
        dim_sizes (Dict[str, int]): A dictionary mapping desired dimension names to their sizes.
        nontaken_axis (str): The dimension along which to expand, no extension into this dim.
        undesirable_dimensions (Dict[str, Any]): A dictionary of dimensions to exclude. variables along these dimensions will not be in the returned dataset
        
    Returns:
        xr.Dataset: The expanded xarray dataset.
    """
    with xr.open_dataset(file) as ds:
        res = expand_dimensions(ds, dim_sizes, nontaken_axis, undesirable_dimensions)
    return res

# --------------------------------------------------------