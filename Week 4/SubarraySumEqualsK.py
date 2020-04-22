"""
Task 22:
    Given an array of integers and an integer k, you need to find the total 
    number of continuous subarrays whose sum equals to k.

    Example:
    Input:nums = [1,1,1], k = 2
    Output: 2
    Note:
    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the 
    integer k is [-1e7, 1e7].
"""
# Time Limit Exceeded

class Solution:
    #def subarraySum(self, nums: List[int], k: int) -> int:
     def subarraySum(nums, k):   
        counter = 0
        length = len(nums)
        for i in range(length):
            s = 0
            for j in range(i, length):
                s += nums[j]
                if s == k:
                    counter+=1
        return counter

#Tests
nums = [1,2,3]
k = 3
print(Solution.subarraySum(nums, k), "2")
nums = [-1,-1,2]
k = 2
print(Solution.subarraySum(nums, k), "1")
nums = [100,1,2,3,4]
k = 6
print(Solution.subarraySum(nums, k), "1")
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
k = 2
print(Solution.subarraySum(nums, k), "36") 
