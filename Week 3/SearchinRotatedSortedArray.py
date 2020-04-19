"""
Suppose an array sorted in ascending order is rotated at some pivot unknown 
to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, 
otherwise return -1.
You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""
#Difficulty: Medium
#196 / 196 test cases passed.
#Runtime: 76 ms
#Memory Usage: 14.1 MB

class Solution:
    #def search(self, nums: List[int], target: int) -> int:
    def search(nums, target):
        l, r = 0, len(nums)-1
        if len(nums) == 0: return -1
        if len(nums) <= 2: 
            return nums.index(target) if target in nums else -1
        if len(nums) > 2:
            m = [i for i in range(len(nums)) if nums[i] < nums[i-1]][-1]
            if m == 0:
                m = (l + r)//2
        else:
            return -1
        if nums[0] <= target <= nums[m-1]:
            return Solution.binarySearch(nums[:m], target)
        else:
            result = Solution.binarySearch(nums[m:], target)
            return m + result if result != -1 else -1
            
    def binarySearch(nums, target):        
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r)//2    
            search = nums[m]
            if search == target:
                return m
            if search > target:
                r = m - 1
            else:
                l = m + 1
        return -1
 
#Tests       
nums = [4,5,6,7,0,1,2]
target = 0
print(Solution.binarySearch(nums, target))
nums = [4,5,6,7,0,1,2]
target = 3
print(Solution.binarySearch(nums, target))
