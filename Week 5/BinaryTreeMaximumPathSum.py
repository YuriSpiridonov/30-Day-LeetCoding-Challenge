"""
Task 29:
    Given a non-empty binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some 
    starting node to any node in the tree along the parent-child connections. 
    The path must contain at least one node and does not need to go through 
    the root.

    Example:
    Input: [-10,9,20,null,null,15,7]
    
       -10
       / \
      9  20
        /  \
       15   7
    
    Output: 42
"""
#93 / 93 test cases passed.
#Runtime: 104 ms
#Memory Usage: 20.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.sum = -9999999999 #float('-inf')
        self.getSum(root)
        return self.sum

    def getSum(self, root):
        if root is None: return 0
        left = self.getSum(root.left)
        right = self.getSum(root.right)
        max_in_node = max(max(left, right) + root.val, root.val)
        max_sum = max(max_in_node, left + right + root.val)
        self.sum = max(self.sum, max_sum)
        return max_in_node
