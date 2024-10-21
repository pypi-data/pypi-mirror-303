import pandas as pd
from dataframe import LazyDataFrame

def read_csv(filepath, **kwargs):
    # Load data into a LazyDataFrame
    data = pd.read_csv(filepath, **kwargs)
    return LazyDataFrame(data)

def read_parquet(filepath, **kwargs):
    # Load data into a LazyDataFrame
    data = pd.read_parquet(filepath, **kwargs)
    return LazyDataFrame(data)
