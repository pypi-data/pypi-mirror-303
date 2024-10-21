import pandas as pd
import numpy as np

# create a callable template for the sampling functions
from typing import Callable, Tuple

# Define a type alias for the sampler function signature
SamplerFunction = Callable[..., Tuple[pd.DataFrame, ...]]

# key idea: samplers are functions that take a dataframe and return a sampled dataframe
# the sampler functions are stored in a dictionary, and the dictionary is used to get the sampler function by name - making it easy to add new samplers later

def sample_with_replacement(*dfs: pd.DataFrame) -> tuple[pd.DataFrame]:
    """
    Sample from the input dataframes with replacement.
    
    Args:
        *dfs (pd.DataFrame): Input dataframes
    
    Returns:
        List[pd.DataFrame]: List of sampled dataframes with the same number of rows as the inputs
    
    Raises:
        ValueError: If the input dataframes have different numbers of rows
    """
    if len(dfs) == 0:
        return []
    
    row_counts = [len(df) for df in dfs]
    if len(set(row_counts)) != 1:
        raise ValueError("All input dataframes must have the same number of rows")
    
    n_rows = row_counts[0]
    random_state = np.random.RandomState()
    sampled_indices = random_state.choice(n_rows, size=n_rows, replace=True)
    
    return (df.iloc[sampled_indices].reset_index(drop=True) for df in dfs)

def sample_without_replacement(*dfs: pd.DataFrame) -> tuple[pd.DataFrame]:
    """
    Sample from the input dataframes without replacement.
    
    Args:
        *dfs (pd.DataFrame): Input dataframes
    
    Returns:
        List[pd.DataFrame]: List of sampled dataframes with the same number of rows as the inputs
    
    Raises:
        ValueError: If the input dataframes have different numbers of rows
    """
    if len(dfs) == 0:
        return []
    
    row_counts = [len(df) for df in dfs]
    if len(set(row_counts)) != 1:
        raise ValueError("All input dataframes must have the same number of rows")
    
    n_rows = row_counts[0]
    random_state = np.random.RandomState()
    sampled_indices = random_state.permutation(n_rows)
    
    return (df.iloc[sampled_indices].reset_index(drop=True) for df in dfs)

SAMPLERS = {
    "with_replacement": sample_with_replacement,
    "without_replacement": sample_without_replacement,
}


def get_sampler(name: str) -> callable:
    """
    Get the sampler function by name.
    
    Args:
        name (str): Name of the sampler
    
    Returns:
        callable: Sampler function
    
    Raises:
        ValueError: If the name is not a valid sampler
    """
    if name not in SAMPLERS:
        raise ValueError(f"Invalid sampler name: {name}")
    return SAMPLERS[name]