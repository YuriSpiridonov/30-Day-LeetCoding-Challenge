"""
Task 28:
    You have a queue of integers, you need to retrieve the first unique integer 
    in the queue.
    Implement the FirstUnique class:
        -FirstUnique(int[] nums) Initializes the object with the numbers in the 
         queue.
        -int showFirstUnique() returns the value of the first unique integer of 
        -the queue, and returns -1 if there is no such integer.
         void add(int value) insert value to the queue.
    Example 1:

    Input: 
    ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
    [[[2,3,5]],[],[5],[],[2],[],[3],[]]
    Output: 
    [null,2,null,2,null,3,null,-1]
    Explanation: 
    FirstUnique firstUnique = new FirstUnique([2,3,5]);
    firstUnique.showFirstUnique(); // return 2
    firstUnique.add(5);            // the queue is now [2,3,5,5]
    firstUnique.showFirstUnique(); // return 2
    firstUnique.add(2);            // the queue is now [2,3,5,5,2]
    firstUnique.showFirstUnique(); // return 3
    firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
    firstUnique.showFirstUnique(); // return -1     
"""
#Time Limit Exceeded

from collections import OrderedDict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.od = OrderedDict()
        for num in self.nums:
            self.od[num] = self.nums.count(num)

    def showFirstUnique(self) -> int:
        for value, count in self.od.items():
            if count == 1: return value
        return -1

    def add(self, value: int) -> None:
        if value in self.nums:
            self.od[value] += 1
        else: self.od[value] = 1
        self.nums.append(value)
