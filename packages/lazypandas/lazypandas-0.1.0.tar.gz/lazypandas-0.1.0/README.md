# LazyPandas

LazyPandas is a high-performance Python library that extends the familiar Pandas DataFrame functionality with lazy evaluation, adaptive execution, and parallel processing capabilities. It provides a familiar API while optimizing operations to deliver significant performance improvements for large datasets and complex data transformations.

## Key Features

- **Lazy Evaluation**: Operations are deferred until needed, allowing for optimized execution plans and reduced redundant calculations.
- **Adaptive Execution**: Automatically selects between parallel and sequential execution based on the dataset size, utilizing multi-threading for large datasets.
- **Operation Caching**: Intelligent caching mechanisms to avoid recalculating repeated operations.
- **Parallel Processing**: Supports parallel execution for many operations, leveraging multiple CPU cores to speed up processing.
- **Execution Plan Optimization**: Reorders operations for better performance based on cost-based optimization techniques.
- **Better Handling of Large Datasets**: Out-of-core processing, memory-mapped file support, and adaptive chunk management for datasets larger than memory.
- **Time-Series and Advanced Operations**: Optimized support for time-series functions and multi-level groupby.
- **Machine Learning Integration**: Data preparation utilities for ML libraries like PyTorch, with built-in support for data batching.

## Installation

You can install LazyPandas from PyPI:

```bash
pip install lazypandas
