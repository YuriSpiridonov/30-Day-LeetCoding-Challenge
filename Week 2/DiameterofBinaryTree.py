"""
Task 11:
    Given a binary tree, you need to compute the length of the diameter of the tree. 
    The diameter of a binary tree is the length of the longest path between 
    any two nodes in a tree. This path may or may not pass through the root.

    Example:
    Given a binary tree
              1
             / \
            2   3
           / \     
          4   5    
    Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
    
    Note: The length of path between two nodes is represented by 
    the number of edges between them.
"""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth = 1
        self.getDepth(root)
        return self.depth - 1

    def getDepth(self, root):
        if root is None: return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        self.depth = max(self.depth, left+right+1)
        return max(left, right) + 1 
