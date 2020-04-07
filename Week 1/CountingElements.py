"""
Task 7:
    Given an integer array arr, count element x such that x + 1 is also in arr.
    If there're duplicates in arr, count them seperately.
    
    Example:
    Input: arr = [1,3,2,3,5,0]
    Output: 3
    Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
"""

class Solution:
    #def countElements(self, arr: List[int]) -> int:
    def countElements(arr):
        return len([item for item in arr if item+1 in arr])       
                
# Tests
arr = [1,2,3] #2
print(Solution.countElements(arr))
arr = [1,1,3,3,5,5,7,7] #0
print(Solution.countElements(arr))
arr = [1,3,2,3,5,0] #3
print(Solution.countElements(arr))
arr = [1,1,2,2] #2
print(Solution.countElements(arr))
