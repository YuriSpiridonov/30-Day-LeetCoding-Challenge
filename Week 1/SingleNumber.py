"""
Task 1:
    Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution:
    #def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(nums):    
        nums_set = set(nums)
        for num in nums_set:
            if nums.count(num) == 1:
                return num

#Tests            
array = [4,1,2,1,2]
print(Solution.singleNumber(array))  
