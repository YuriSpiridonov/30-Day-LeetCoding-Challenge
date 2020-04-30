"""
Task 30:
    Given a binary tree where each path going from the root to any leaf form a 
    valid sequence, check if a given string is a valid sequence in such binary 
    tree. 

    We get the given string from the concatenation of an array of integers arr 
    and the concatenation of all values of the nodes along a path results in a 
    sequence in the given binary tree.
    
    Example:
    Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
    Output: true
    Explanation: 
    The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
    Other valid sequences are: 
    0 -> 1 -> 1 -> 0 
"""
# source https://www.youtube.com/watch?v=23oR5ipWwk8

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.i = 0
        self.length = len(arr)
        if not root: return self.length == 0
        return self.isValid(root, arr, self.i)
   
    def isValid(self, root, arr, i):
        if root.val != arr[i]: return False
        if i == self.length-1: return bool(not root.left and not root.right)
        return bool(root.left and self.isValid(root.left, arr, i+1) or (root.right and self.isValid(root.right, arr, i+1)))
