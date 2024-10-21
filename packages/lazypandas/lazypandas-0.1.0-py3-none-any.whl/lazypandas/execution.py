from concurrent.futures import ThreadPoolExecutor
from optimization import optimize_execution_plan, cache_intermediate_results
import pandas as pd

class ExecutionEngine:
    @staticmethod
    def cost_based_reordering(operations):
        # Assign costs to operations and reorder based on cost
        operation_costs = {
            'filter': 1,  # Low cost
            'merge': 5,   # High cost
            'groupby': 3  # Medium cost
        }
        optimized_operations = sorted(operations, key=lambda op: operation_costs.get(str(op[0]), 0))
        return optimized_operations


    @staticmethod
    def execute(self, lazy_dataframe, num_threads=4):
        # Determine execution strategy based on dataset size
        dataset_size = len(lazy_dataframe.data)
        parallel = dataset_size > 1e6  # Example threshold for large datasets

        # Step 1: Reorder operations
        optimized_operations = optimize_execution_plan(lazy_dataframe.operations)

        # Step 2: Apply caching
        cached_operations = cache_intermediate_results(optimized_operations)

        # Step 3: Execute using the chosen strategy
        if parallel:
            result = self.parallel_execute(cached_operations, lazy_dataframe.data, num_threads)
        else:
            result = lazy_dataframe.data
            for operation, args, kwargs in cached_operations:
                result = operation(result, *args, **kwargs)

        return result

    @staticmethod
    def dynamic_query_planning(operations):
        # Use cost-based optimization to reorder operations
        operation_costs = {
            'filter': 1,
            'merge': 5,
            'apply': 2,
            'groupby': 3,
        }
        return sorted(operations, key=lambda op: operation_costs.get(op[0].__name__, 0))

    @staticmethod
    def parallel_apply(dataframe, func, num_threads=4):
        # Parallel execution of 'apply' function using multiple threads
        chunk_size = len(dataframe) // num_threads
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            results = list(executor.map(lambda chunk: chunk.apply(func), 
                                        [dataframe.iloc[i:i + chunk_size] for i in range(0, len(dataframe), chunk_size)]))
        return pd.concat(results)
    
    @staticmethod
    def parallel_execute(operations, data, num_threads=4):
        """
        Execute operations in parallel using multiple threads.
        """
        chunk_size = len(data) // num_threads
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            results = list(executor.map(lambda chunk: execute_operations(chunk, operations),
                                        [data.iloc[i:i + chunk_size] for i in range(0, len(data), chunk_size)]))
        # Combine the results
        return pd.concat(results)

    @staticmethod
    def execute_operations(chunk, operations):
        """
        Helper function to execute a list of operations on a data chunk.
        """
        result = chunk
        for operation, args, kwargs in operations:
            result = operation(result, *args, **kwargs)
        return result