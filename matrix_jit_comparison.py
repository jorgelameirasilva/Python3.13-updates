import numpy as np
import time
import os
from typing import List, Tuple
import platform

def matrix_multiply_pure_python(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Pure Python implementation of matrix multiplication."""
    if len(a[0]) != len(b):
        raise ValueError("Matrix dimensions don't match")
    
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    
    result = [[0.0] * cols_b for _ in range(rows_a)]
    
    # This is the hot loop that JIT should optimize
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    
    return result

def benchmark_multiplication(size: int, runs: int = 5) -> Tuple[float, float]:
    """Benchmark matrix multiplication with and without NumPy."""
    # Create random matrices
    matrix_a = [[float(np.random.rand()) for _ in range(size)] for _ in range(size)]
    matrix_b = [[float(np.random.rand()) for _ in range(size)] for _ in range(size)]
    
    # NumPy benchmark
    np_a = np.array(matrix_a)
    np_b = np.array(matrix_b)
    
    numpy_times = []
    python_times = []
    
    for _ in range(runs):
        # Time NumPy multiplication
        start = time.perf_counter()
        np.dot(np_a, np_b)
        numpy_times.append(time.perf_counter() - start)
        
        # Time pure Python multiplication
        start = time.perf_counter()
        matrix_multiply_pure_python(matrix_a, matrix_b)
        python_times.append(time.perf_counter() - start)
    
    return (
        sum(python_times) / runs,  # Average Python time
        sum(numpy_times) / runs    # Average NumPy time
    )

def main():
    # Check if JIT is enabled
    jit_enabled = os.environ.get('PYTHON_JIT', '0') == '1'
    python_version = platform.python_version()
    
    print(f"Python Version: {python_version}")
    print(f"JIT Enabled: {jit_enabled}")
    print("\nBenchmarking matrix multiplication...")
    print("-" * 50)
    
    sizes = [50, 100, 200, 400]
    
    for size in sizes:
        print(f"\nMatrix size: {size}x{size}")
        python_time, numpy_time = benchmark_multiplication(size)
        
        print(f"Pure Python time: {python_time:.4f} seconds")
        print(f"NumPy time:      {numpy_time:.4f} seconds")
        print(f"Python/NumPy ratio: {python_time/numpy_time:.2f}x slower")

if __name__ == "__main__":
    main() 