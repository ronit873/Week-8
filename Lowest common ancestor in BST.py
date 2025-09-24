class Solution:

    def LCA(self, root, n1, n2):

        if root.data>n1.data and root.data>n2.data:

            return self.LCA(root.left,n1,n2)

        if root.data<n1.data and root.data<n2.data:

            return self.LCA(root.right,n1,n2)

        return root
    