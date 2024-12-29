import ast
from timespacex.analyzer import BigOAnalyzer

def test_simple_loop():
    code = """
def sum_elements(arr):
    total = 0
    for element in arr:
        total += element
    return total
"""
    tree = ast.parse(code)
    analyzer = BigOAnalyzer()
    analyzer.visit(tree)
    
    result = analyzer.analyzed_functions['sum_elements']
    assert result['time_complexity'] == "O(n)"
    assert result['space_complexity'] == "O(1)"

def test_nested_loops():
    code = """
def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] 
              for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
"""
    tree = ast.parse(code)
    analyzer = BigOAnalyzer()
    analyzer.visit(tree)
    
    result = analyzer.analyzed_functions['matrix_multiplication']
    assert result['time_complexity'] == "O(n³)"
    assert 'three nested loops' in result['explanation'].lower()

def test_binary_search():
    code = """
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
"""
    tree = ast.parse(code)
    analyzer = BigOAnalyzer()
    analyzer.visit(tree)
    
    result = analyzer.analyzed_functions['binary_search']
    assert result['time_complexity'] == "O(log n)"
    assert result['space_complexity'] == "O(1)"

def test_recursive_function():
    code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
    tree = ast.parse(code)
    analyzer = BigOAnalyzer()
    analyzer.visit(tree)
    
    result = analyzer.analyzed_functions['fibonacci']
    assert result['time_complexity'] == "O(2^n)"
    assert result['space_complexity'] == "O(n)"
    assert 'recursive' in result['explanation'].lower()

def test_space_complexity_with_growing_ds():
    code = """
def create_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]
"""
    tree = ast.parse(code)
    analyzer = BigOAnalyzer()
    analyzer.visit(tree)
    
    result = analyzer.analyzed_functions['create_matrix']
    assert result['space_complexity'] == "O(n)"
    assert 'grows' in result['explanation'].lower() 