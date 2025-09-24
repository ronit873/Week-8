class Solution:
    
    def insert(self,root, Key):
        if root is None:
            return Node(Key)
        if root.data > Key:
            root.left = self.insert(root.left,Key)
        elif root.data<Key:
            root.right = self.insert(root.right,Key)
        return 
    