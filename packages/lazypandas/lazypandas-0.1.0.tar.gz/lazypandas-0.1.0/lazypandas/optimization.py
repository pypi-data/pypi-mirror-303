def optimize_execution_plan(operations):
    """
    Reorder operations in the execution plan to optimize performance.
    - Filters and selections should be performed early.
    - Expensive operations like joins and aggregations should be deferred.
    """
    # Assign a cost to each type of operation
    operation_costs = {
        'filter': 1,  # Low cost
        'select': 1,  # Low cost
        'groupby': 3, # Medium cost
        'merge': 5,   # High cost
        'aggregate': 4, # Medium-high cost
        'join': 5     # High cost
    }

    # Sort operations based on their cost, lower cost operations are executed first
    optimized_operations = sorted(operations, key=lambda op: operation_costs.get(op[0].__name__, 0))
    return optimized_operations

def cache_intermediate_results(operations):
    """
    Cache intermediate results to avoid recalculating them when
    the same operations are performed multiple times.
    """
    cached_results = {}
    new_operations = []

    for op in operations:
        if op in cached_results:
            # Skip operation if result is already cached
            continue
        else:
            # Add operation to execution plan and cache the result
            new_operations.append(op)
            cached_results[op] = True  # Mark as cached

    return new_operations
