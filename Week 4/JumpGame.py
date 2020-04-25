"""
Task 25:
    Given an array of non-negative integers, you are initially positioned at 
    the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    
    Example:
    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
#Difficulty: Medium
#75 / 75 test cases passed.
#Runtime: 92 ms
#Memory Usage: 16 MB

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        m = nums[0]
        length = len(nums)-1
        for i in range(length):
            if m <= i and nums[i] == 0:
                 return False
            if i + nums[i] > m:
                m = i + nums[i]
        if m >= length:
            return True
        return False
