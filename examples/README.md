# TimeSpaceX Examples

This directory contains example Python files that demonstrate various algorithms and data structures, along with their time and space complexity analysis.

## Sorting Algorithms (`sorting_algorithms.py`)

Contains implementations of common sorting algorithms:
- Bubble Sort: O(n²) time, O(1) space
- Merge Sort: O(n log n) time, O(n) space
- Quick Sort: O(n log n) average time, O(log n) space

## Data Structures (`data_structures.py`)

Contains implementations of common data structures:
- Linked List
  - Insertion at beginning: O(1) time
  - Search: O(n) time
  - Space: O(n)
- Binary Search Tree
  - Insertion: O(log n) time (balanced)
  - Search: O(log n) time (balanced)
  - Space: O(n)
- Max Heap
  - Insertion: O(log n) time
  - Get Max: O(1) time
  - Space: O(n)

## Using TimeSpaceX with Examples

You can analyze any of these files using TimeSpaceX:

```bash
timespacex sorting_algorithms.py
timespacex data_structures.py
```

This will provide a detailed analysis of the time and space complexity for each function and class method in the files. 