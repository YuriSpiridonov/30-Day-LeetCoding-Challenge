"""
Taskk 4:
    Given an array nums, write a function to move all 0's to the end of it 
    while maintaining the relative order of the non-zero elements.

    Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""
    
class Solution:
    #def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(nums):    
        nums.sort(key=lambda x:x==0)

#Tests
nums = [0,1,0,3,12]
print(Solution.moveZeroes(nums))
nums = [0,1,0,3,12,4,5,6,0,9,8,0,9,0,23,4,5,0,0,0,4] 
print(Solution.moveZeroes(nums))
