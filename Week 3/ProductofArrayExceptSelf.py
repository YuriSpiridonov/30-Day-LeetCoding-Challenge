"""
Task 15:
    Given an array nums of n integers where n > 1,  
    return an array output such that output[i] is equal to 
    the product of all the elements of nums except nums[i].
    
    Example:
    Input:  [1,2,3,4]
    Output: [24,12,8,6]
"""
#Difficulty: Medium
#31 / 31 test cases passed.
#Runtime: 120 ms
#Memory Usage: 18.2 MB

#Runtime: 120 ms, faster than 85.97% of Python3 online submissions for Product of Array Except Self.
#Memory Usage: 18.2 MB, less than 100.00% of Python3 online submissions for Product of Array Except Self.
import math

class Solution:
    #def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(nums):    
        nums_set, d = set(nums), {0:0}
        for s in nums_set:
            d[s] = math.prod(nums[:nums.index(s)] + nums[nums.index(s)+1:])
        for i in range(len(nums)):
            if nums[i] in d.keys(): nums[i] = d[nums[i]]
        return nums
    
#Tests
nums = [1,-1]
print(Solution.productExceptSelf(nums), '[-1,1]')
nums = [0,0]
print(Solution.productExceptSelf(nums), '[0,0]')
nums = [1,2,3,4,3]
print(Solution.productExceptSelf(nums), '[72,36,24,18,24]')
nums = [1,2,3,4]
print(Solution.productExceptSelf(nums), '[24,12,8,6]')
nums = [1,2,3,4,5,4,3,2,5,3]
print(Solution.productExceptSelf(nums), '[43200,21600,14400,10800,8640,10800,14400,21600,8640,14400]')
