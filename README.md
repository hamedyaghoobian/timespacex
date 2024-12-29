# TimeSpaceX 🚀

[![PyPI version](https://badge.fury.io/py/timespacex.svg)](https://badge.fury.io/py/timespacex)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful Python Time and Space Complexity Analyzer that helps you understand the computational complexity of your code. TimeSpaceX analyzes your Python functions and provides detailed explanations of their time and space complexity using Big O notation.

## ✨ Features

- 📊 Analyzes both time and space complexity
- 📝 Provides detailed explanations for each analysis
- 🎯 Detects common algorithmic patterns:
  - Simple loops `O(n)`
  - Nested loops `O(n²)`, `O(n³)`
  - Binary search patterns `O(log n)`
  - Divide and conquer algorithms `O(n log n)`
  - Recursive functions
  - Matrix operations
- 🎨 Beautiful command-line interface with syntax highlighting
- 🔍 Smart pattern recognition for common algorithms
- 💡 Educational tool for learning algorithmic complexity

## 🚀 Quick Start

### Installation

```bash
pip install timespacex
```

### Usage

Analyze a Python file:
```bash
timespacex your_file.py
```

Options:
```bash
timespacex --no-color your_file.py  # Disable colored output
```

## 📚 Examples

### Example 1: Simple Loop Analysis

```python
def sum_elements(arr):
    total = 0
    for element in arr:
        total += element
    return total
```

Output:
```
╭─ Function: sum_elements ──────────────────────╮
│ The function `sum_elements` has a time        │
│ complexity of O(n). This is because the       │
│ function iterates through the input exactly   │
│ once.                                         │
│                                              │
│ The space complexity is O(1). This is because│
│ the function uses a constant amount of extra  │
│ space regardless of input size.              │
╰──────────────────────────────────────────────╯
```

### Example 2: Binary Search Analysis

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

Output:
```
╭─ Function: binary_search ──────────────────────╮
│ The function `binary_search` has a time        │
│ complexity of O(log n). This is because the    │
│ function uses a binary search pattern,         │
│ dividing the search space in half at each      │
│ step.                                          │
│                                               │
│ The space complexity is O(1). This is because │
│ the function uses a constant amount of extra   │
│ space regardless of input size.               │
╰───────────────────────────────────────────────╯
```

### Example 3: Matrix Operations

```python
def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] 
              for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
```

Output:
```
╭─ Function: matrix_multiplication ─────────────╮
│ The function `matrix_multiplication` has a    │
│ time complexity of O(n³). This is because    │
│ the function performs matrix multiplication   │
│ with three nested loops.                     │
│                                             │
│ The space complexity is O(n²). This is      │
│ because the function creates a new matrix    │
│ that grows quadratically with input size.   │
╰─────────────────────────────────────────────╯
```

## 🔍 Supported Patterns

TimeSpaceX can detect and analyze:

- ⏱ Time Complexity Patterns:
  - Linear iterations `O(n)`
  - Nested loops `O(n²)`, `O(n³)`
  - Binary search `O(log n)`
  - Divide and conquer `O(n log n)`
  - Recursive patterns
  - Matrix operations
  - Exponential complexity `O(2^n)`

- 💾 Space Complexity Patterns:
  - Constant space `O(1)`
  - Linear space `O(n)`
  - Quadratic space `O(n²)`
  - Recursive stack space
  - Dynamic array growth
  - Matrix space requirements

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [bigocalc.com](https://www.bigocalc.com/)
- Built with [rich](https://github.com/Textualize/rich) for beautiful terminal output

## 📫 Contact

Hamed Yaghoobian - hamedyaghoobian@gmail.com

Project Link: [https://github.com/hamedyaghoobian/timespacex](https://github.com/hamedyaghoobian/timespacex) 