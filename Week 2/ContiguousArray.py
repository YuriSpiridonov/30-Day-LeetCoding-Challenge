"""
Task 13:
    Given a binary array, find the maximum length of a contiguous subarray 
    with equal number of 0 and 1.

    Example:
    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with 
    equal number of 0 and 1.
"""

class Solution:
    #def findMaxLength(self, nums: List[int]) -> int:
    def findMaxLength(nums):    
        c, l, ln = 0, 0, {0: 0}
        for i, n in enumerate(nums, 1):
            c += 1 if n == 1 else -1
            if c in ln: l = max(l, i - ln[c])
            else: ln[c] = i
        return l

#Tests
nums = [0,1]
print(Solution.findMaxLength(nums), '2')
nums = [0,1,0,1,0,1]
print(Solution.findMaxLength(nums), '6')
nums = [0,1,0,1,0,1,0,0,1,0,1]
print(Solution.findMaxLength(nums), '10')
nums = [0,1,0,1,0,1,0,0,0,0,1]
print(Solution.findMaxLength(nums), '6')
nums = [0,1,0,1,0,1,0,0,0,0,1,0]
print(Solution.findMaxLength(nums), '6')
nums = [0,1,0,1,0,1,0,0,0,0,1,0,1]
print(Solution.findMaxLength(nums), '6')
nums = [0,1,0,1,0,1,0,0,0,0,1,0,1,0]
print(Solution.findMaxLength(nums), '6')
nums = [0,1,0,1,0,1,0,0,0,0,1,0,1,0,1]
print(Solution.findMaxLength(nums), '6')
nums = [0,1,0,1,0,1,0,0,0,1,0,1,0,1]
print(Solution.findMaxLength(nums), '6')
nums = [0,1,0,1,0,1,0,0,1,0,1,0,1]
print(Solution.findMaxLength(nums), '12')
nums = [0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1] 
print(Solution.findMaxLength(nums), '10')
