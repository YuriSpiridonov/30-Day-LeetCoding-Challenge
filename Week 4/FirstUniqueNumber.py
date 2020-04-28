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
#17 / 17 test cases passed.
#Runtime: 1512 ms
#Memory Usage: 54.6 MB

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = dict()
        self.queue = list()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while len(self.queue) > 0 and self.d[self.queue[0]] > 1:
            self.queue.pop(0)
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]

    def add(self, value: int) -> None:
        if value in self.d.keys():
            self.d[value] += 1
        else: 
            self.d[value] = 1
            self.queue.append(value)
