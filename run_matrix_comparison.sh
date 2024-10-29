#!/bin/bash

echo "Running matrix multiplication benchmark without JIT..."
PYTHON_JIT=0 python3.13 matrix_jit_comparison.py

echo -e "\n----------------------------------------\n"

echo "Running matrix multiplication benchmark with JIT..."
PYTHON_JIT=1 python3.13 matrix_jit_comparison.py