import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import psutil

class LazyDataFrame:

    def __init__(self, data=None):
        self.data = data
        self.operations = []
        self.cache = {}


    def add_operation(self, operation, *args, **kwargs):
        # Add the operation to the list of deferred operations
        self.operations.append((operation, args, kwargs))
        self.invalidate_cache()  # Invalidate cache when a new operation is added


    def execute(self):
        # Generate a unique cache key based on the operations
        cache_key = tuple((op[0].__name__, tuple(op[1]), tuple(sorted(op[2].items()))) for op in self.operations)
        if cache_key in self.cache:
            # Return cached result if available
            return self.cache[cache_key]

        # Execute all operations
        result = self.data
        for operation, args, kwargs in self.operations:
            result = operation(result, *args, **kwargs)

        # Cache the result of the current operations
        self.cache[cache_key] = result
        return result
    

    def invalidate_cache(self):
        # Clear the cache if the operations have changed
        self.cache.clear()

        
    def head(self, n=5):
        self.add_operation(lambda df: df.head(n))
        return self

    def tail(self, n=5):
        self.add_operation(lambda df: df.tail(n))
        return self

    def filter(self, condition):
        self.add_operation(lambda df: df[condition])
        return self

    def select(self, columns):
        self.add_operation(lambda df: df[columns])
        return self

    def drop(self, columns):
        self.add_operation(lambda df: df.drop(columns, axis=1))
        return self

    def groupby(self, column):
        self.add_operation(lambda df: df.groupby(column))
        return self

    def sum(self):
        self.add_operation(lambda df: df.sum())
        return self

    def mean(self):
        self.add_operation(lambda df: df.mean())
        return self

    def merge(self, other, on=None, how='inner'):
        self.add_operation(lambda df: df.merge(other.data, on=on, how=how))
        return self

    def vectorized_sum(self, column):
        self.add_operation(lambda df: np.sum(df[column].values))
        return self

    def vectorized_mean(self, column):
        self.add_operation(lambda df: np.mean(df[column].values))
        return self
    
    def parallel_filter(self, condition, num_threads=4):
        # Split data into chunks and apply filter in parallel
        chunk_size = len(self.data) // num_threads
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            filtered_chunks = list(executor.map(lambda chunk: chunk[condition], 
                                                [self.data[i:i + chunk_size] for i in range(0, len(self.data), chunk_size)]))
        # Combine filtered chunks back together
        self.data = pd.concat(filtered_chunks)
        return self
    
    def parallel_merge(self, other, on=None, how='inner', num_threads=4):
        # Split data into chunks and perform merge in parallel
        chunk_size = len(self.data) // num_threads
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            merged_chunks = list(executor.map(lambda chunk: chunk.merge(other.data, on=on, how=how),
                                              [self.data[i:i + chunk_size] for i in range(0, len(self.data), chunk_size)]))
        # Combine merged chunks back together
        self.data = pd.concat(merged_chunks)
        return self


    def parallel_groupby_apply(self, groupby_column, func, num_threads=4):
        # Split data into chunks and perform groupby-apply in parallel
        chunk_size = len(self.data) // num_threads
        with ProcessPoolExecutor(max_workers=num_threads) as executor:
            results = list(executor.map(lambda chunk: chunk.groupby(groupby_column).apply(func),
                                        [self.data[i:i + chunk_size] for i in range(0, len(self.data), chunk_size)]))
        # Combine results back together
        self.data = pd.concat(results)
        return self



    def read_csv_in_chunks(filepath, chunk_size=10000):
        # Load data in chunks
        chunks = pd.read_csv(filepath, chunksize=chunk_size)
        return LazyDataFrame(pd.concat(chunks))

    def memory_map(self, filepath):
        # Load a large file as a memory-mapped object
        self.data = pd.read_csv(filepath, memory_map=True)
        return self


    def std(self, column):
        self.add_operation(lambda df: np.std(df[column].values))
        return self

    def var(self, column):
        self.add_operation(lambda df: np.var(df[column].values))
        return self

    def min(self, column):
        self.add_operation(lambda df: np.min(df[column].values))
        return self

    def max(self, column):
        self.add_operation(lambda df: np.max(df[column].values))
        return self
    
    def pivot(self, index, columns, values):
        self.add_operation(lambda df: df.pivot(index=index, columns=columns, values=values))
        return self

    def melt(self, id_vars, value_vars):
        self.add_operation(lambda df: pd.melt(df, id_vars=id_vars, value_vars=value_vars))
        return self

    def resample(self, rule):
        self.add_operation(lambda df: df.resample(rule))
        return self
    
    def read_csv_in_chunks(self, filepath, chunk_size=10000, memory_pool=None):
        # Read CSV in chunks and store in memory pool
        chunks = pd.read_csv(filepath, chunksize=chunk_size)
        if memory_pool:
            for chunk in chunks:
                memory_pool.allocate(chunk.memory_usage().sum())
            self.data = pd.concat(chunks)
        else:
            self.data = pd.concat(chunks)
        return self
    

    def stack(self):
        self.add_operation(lambda df: df.stack())
        return self

    def unstack(self, level=-1):
        self.add_operation(lambda df: df.unstack(level))
        return self

    def rolling(self, window, min_periods=1):
        self.add_operation(lambda df: df.rolling(window=window, min_periods=min_periods))
        return self

    def expanding(self, min_periods=1):
        self.add_operation(lambda df: df.expanding(min_periods=min_periods))
        return self

    def cov(self):
        self.add_operation(lambda df: df.cov())
        return self

    def corr(self, method='pearson'):
        self.add_operation(lambda df: df.corr(method=method))
        return self


    def adaptive_chunk_size(self, base_size=10000, memory_limit=1e9):
        # Adjust chunk size based on the available memory
        available_memory = self.get_available_memory()
        adjusted_size = min(base_size, int(memory_limit / (self.data.memory_usage().sum() / len(self.data))))
        return adjusted_size

    def get_available_memory(self):
        # Use psutil to get available system memory
        memory_info = psutil.virtual_memory()
        return memory_info.available  # Returns the available memory in bytes


    def to_tensor(self, target_column=None):
        # Convert the dataframe to a PyTorch tensor
        import torch
        data = self.data.drop(columns=[target_column]).values if target_column else self.data.values
        target = self.data[target_column].values if target_column else None
        return torch.tensor(data, dtype=torch.float32), torch.tensor(target, dtype=torch.float32) if target else None

    def batch(self, batch_size):
        # Generator for batching data
        for start in range(0, len(self.data), batch_size):
            yield self.data.iloc[start:start + batch_size]


class MemoryPool:
    def __init__(self):
        self.pool = []

    def allocate(self, size):
        # Allocate memory block of given size
        memory_block = bytearray(size)
        self.pool.append(memory_block)
        return memory_block

    def free(self):
        # Clear the memory pool
        self.pool = []

