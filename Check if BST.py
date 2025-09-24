class Solution:
    
    def inOrder(self, root):
        if not root:
            return []
        arr = []
        arr += self.inOrder(root.left)
        arr.append(root.data)
        arr += self.inOrder(root.right)
        return arr
    
    def isBST(self, root):
        arr = self.inOrder(root)
        new_arr = arr[:]
        new_arr.sort()
        return new_arr == arr