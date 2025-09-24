class Solution:
    def LeftView(self, root):
        
        self.levels_visited = set()
        self.leftView = []
        self.getLeftNodes(root, level=0)
        return self.leftView
    def getLeftNodes(self, node, level):
        if node: 
            
            if level not in self.levels_visited:
                self.levels_visited.add(level)
                self.leftView.append(node.data)
            self.getLeftNodes(node.left, level+1)
            self.getLeftNodes(node.right, level+1)