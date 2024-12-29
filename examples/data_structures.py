class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Common operations time complexity:
    - Insertion at beginning: O(1)
    - Insertion at end: O(n)
    - Search: O(n)
    - Deletion: O(n)
    Space Complexity: O(n)
    """
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

class BinarySearchTree:
    """
    Common operations time complexity (balanced tree):
    - Insertion: O(log n)
    - Search: O(log n)
    - Deletion: O(log n)
    Space Complexity: O(n)
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)
    
    def search(self, key):
        if self.data == key:
            return True
        elif key < self.data and self.left:
            return self.left.search(key)
        elif key > self.data and self.right:
            return self.right.search(key)
        return False

class MaxHeap:
    """
    Common operations time complexity:
    - Insertion: O(log n)
    - Extract Max: O(log n)
    - Get Max: O(1)
    Space Complexity: O(n)
    """
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0] 