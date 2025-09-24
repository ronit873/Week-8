class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def mirror(self, root):
        if root is None:
            return
        self.mirror(root.left)
        self.mirror(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp 
        
    def levelOrder(root):
        if root is None:
            print("N ",end="")
            return
        
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            
            if curr is None:
                print("N ",end="")
                continue