import time
import numpy as np
import pandas as pd
import polars as pl
from io_module import read_csv

def benchmark_operations(file_path):
    # Benchmark basic operations like head, filter, and aggregation
    df = pd.read_csv(file_path)
    
    # Select numeric columns for the filter operation
    numeric_cols = df.select_dtypes(include=['number']).columns
    if 'column' in numeric_cols:
        start_time = time.time()
        result = df.head(10).loc[df['column'] > 0].sum()
        pandas_time = time.time() - start_time
    else:
        print("The 'column' is not numeric in the dataset.")
        return

    lazy_df = read_csv(file_path)
    start_time = time.time()
    lazy_result = lazy_df.head(10).filter(lambda df: df['column'] > 0).sum().execute()
    lazy_pandas_time = time.time() - start_time

    print(f"Pandas time: {pandas_time:.4f} seconds")
    print(f"LazyPandas time: {lazy_pandas_time:.4f} seconds")


def benchmark_groupby_operations(file_path):
    df = pd.read_csv(file_path)
    start_time = time.time()
    result = df.groupby('column').sum()
    pandas_time = time.time() - start_time

    lazy_df = read_csv(file_path)
    start_time = time.time()
    lazy_result = lazy_df.groupby('column').sum().execute()
    lazy_pandas_time = time.time() - start_time

    print(f"Pandas groupby: {pandas_time:.4f} seconds")
    print(f"LazyPandas groupby: {lazy_pandas_time:.4f} seconds")


def benchmark_polars_vs_lazypandas(file_path):
    # Benchmark Polars
    start_time = time.time()
    polars_df = pl.read_csv(file_path)
    polars_result = polars_df.group_by("column").sum()
    polars_time = time.time() - start_time

    # Benchmark LazyPandas
    lazy_df = read_csv(file_path)
    start_time = time.time()
    lazy_result = lazy_df.groupby("column").sum().execute()
    lazy_pandas_time = time.time() - start_time

    print(f"Polars groupby: {polars_time:.4f} seconds")
    print(f"LazyPandas groupby: {lazy_pandas_time:.4f} seconds")


def benchmark_wide_vs_long_data(file_path_wide, file_path_long):
    # Benchmark for wide data
    df_wide = pd.read_csv(file_path_wide)
    start_time = time.time()
    result_wide = df_wide.groupby("column").sum()
    pandas_time_wide = time.time() - start_time

    lazy_df_wide = read_csv(file_path_wide)
    start_time = time.time()
    lazy_result_wide = lazy_df_wide.groupby("column").sum().execute()
    lazy_pandas_time_wide = time.time() - start_time

    # Benchmark for long data
    df_long = pd.read_csv(file_path_long)
    start_time = time.time()
    result_long = df_long.groupby("column").sum()
    pandas_time_long = time.time() - start_time

    lazy_df_long = read_csv(file_path_long)
    start_time = time.time()
    lazy_result_long = lazy_df_long.groupby("column").sum().execute()
    lazy_pandas_time_long = time.time() - start_time

    print(f"Pandas (Wide Data): {pandas_time_wide:.4f} seconds")
    print(f"LazyPandas (Wide Data): {lazy_pandas_time_wide:.4f} seconds")
    print(f"Pandas (Long Data): {pandas_time_long:.4f} seconds")
    print(f"LazyPandas (Long Data): {lazy_pandas_time_long:.4f} seconds")


def create_mock_data(file_path="data.csv", num_rows=100000, num_columns=10, 
                     wide_file_path="data_wide.csv", long_file_path="data_long.csv"):
    """
    Create large numeric mock test data for benchmarking.
    
    :param file_path: Path for the basic mock data CSV file.
    :param num_rows: Number of rows for the basic mock data.
    :param num_columns: Number of columns for the mock data.
    :param wide_file_path: Path for the wide data CSV file.
    :param long_file_path: Path for the long data CSV file.
    """
    # Create a basic dataset with random numbers and a numeric 'column' for filtering and groupby
    data = pd.DataFrame(np.random.randn(num_rows, num_columns), columns=[f"col_{i}" for i in range(num_columns)])
    data['column'] = np.random.randint(0, 100, size=num_rows)  # Add a numeric 'column' for groupby and filtering
    data.to_csv(file_path, index=False)
    print(f"Large basic mock data created at {file_path}")

    # Create a wide dataset with more columns (e.g., 500 columns)
    wide_data = pd.DataFrame(np.random.randn(num_rows, 500), columns=[f"wide_col_{i}" for i in range(500)])
    wide_data['column'] = np.random.randint(0, 100, size=num_rows)  # Add a numeric 'column' for groupby
    wide_data.to_csv(wide_file_path, index=False)
    print(f"Large wide mock data created at {wide_file_path}")

    # Create a long dataset with more rows (e.g., 10 million rows)
    long_data = pd.DataFrame(np.random.randn(num_rows * 100, num_columns), columns=[f"col_{i}" for i in range(num_columns)])
    long_data['column'] = np.random.randint(0, 100, size=num_rows * 100)  # Add a numeric 'column' for groupby
    long_data.to_csv(long_file_path, index=False)
    print(f"Large long mock data created at {long_file_path}")


def main():
    # File paths for benchmarking
    file_path = "data.csv"  # Update with the actual path to your dataset
    file_path_wide = "data_wide.csv"  # Update with the path to your wide data file
    file_path_long = "data_long.csv"  # Update with the path to your long data file

    print("\nBenchmarking Basic Operations:")
    benchmark_operations(file_path)

    print("\nBenchmarking Groupby Operations:")
    benchmark_groupby_operations(file_path)

    print("\nBenchmarking Polars vs. LazyPandas:")
    benchmark_polars_vs_lazypandas(file_path)

    print("\nBenchmarking Wide vs. Long Data:")
    benchmark_wide_vs_long_data(file_path_wide, file_path_long)


def benchmark_multilevel_groupby(file_path):
    df = pd.read_csv(file_path)
    start_time = time.time()
    result = df.groupby(['column', 'col_0']).sum()
    pandas_time = time.time() - start_time

    lazy_df = read_csv(file_path)
    start_time = time.time()
    lazy_result = lazy_df.groupby(['column', 'col_0']).sum().execute()
    lazy_pandas_time = time.time() - start_time

    print(f"Pandas multi-level groupby: {pandas_time:.4f} seconds")
    print(f"LazyPandas multi-level groupby: {lazy_pandas_time:.4f} seconds")


def benchmark_joins(file_path):
    df1 = pd.read_csv(file_path)
    df2 = pd.DataFrame(np.random.randn(len(df1), 5), columns=['join_col', 'val_1', 'val_2', 'val_3', 'val_4'])
    df2['join_col'] = np.random.choice(df1['column'], size=len(df1))

    # Benchmark Pandas join
    start_time = time.time()
    result = df1.merge(df2, left_on='column', right_on='join_col', how='inner')
    pandas_time = time.time() - start_time

    # Benchmark LazyPandas join
    lazy_df1 = read_csv(file_path)
    lazy_df2 = read_csv(file_path)  # Mock for LazyPandas
    start_time = time.time()
    lazy_result = lazy_df1.merge(lazy_df2, left_on='column', right_on='join_col', how='inner').execute()
    lazy_pandas_time = time.time() - start_time

    print(f"Pandas join: {pandas_time:.4f} seconds")
    print(f"LazyPandas join: {lazy_pandas_time:.4f} seconds")


def benchmark_time_series_operations(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')

    # Pandas benchmark
    start_time = time.time()
    result = df.resample('M').sum().rolling(window=3).mean()
    pandas_time = time.time() - start_time

    # LazyPandas benchmark
    lazy_df = read_csv(file_path)
    start_time = time.time()
    lazy_result = lazy_df.resample('M').sum().rolling(window=3).mean().execute()
    lazy_pandas_time = time.time() - start_time

    print(f"Pandas time-series operations: {pandas_time:.4f} seconds")
    print(f"LazyPandas time-series operations: {lazy_pandas_time:.4f} seconds")


if __name__ == "__main__":
    # create_mock_data()
    main()
