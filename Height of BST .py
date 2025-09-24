class Solution:

    def height(self, root):
        
        if not root:
            return -1
        return max(1 + self.height(root.left), 1 + self.height(root.right)) 