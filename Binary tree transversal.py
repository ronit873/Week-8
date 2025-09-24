class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, root):
        self.result = []  
        def traverse(node):
            if node:
                traverse(node.left)
                self.result.append(node.data)
                traverse(node.right)

        traverse(root)
        return self.result

