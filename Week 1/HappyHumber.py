"""
Task 2:
    Write an algorithm to determine if a number n is "happy".
    A happy number is a number defined by the following process: 
    Starting with any positive integer, replace the number by the sum of 
    the squares of its digits, and repeat the process until the number 
    equals 1 (where it will stay), or it loops endlessly in a cycle which 
    does not include 1. Those numbers for which this process ends in 1 
    are happy numbers.
    Return True if n is a happy number, and False if not.
    
    Example:
    Input: 19
    Output: true
    Explanation: 
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
"""

lst = list()
class Solution:
    #def isHappy(self, n: int) -> bool:
    def isHappy(n):    
        global lst 
        if n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n not in lst:
                lst.append(n)
            else:
                lst.clear()
                return False
            #return Solution.isHappy(self, n)
            return Solution.isHappy(n)
        elif n == 1:
            lst.clear()
            return True    

#Tests           
s = Solution
n = 19
print(s.isHappy(n))
n = 20
print(s.isHappy(n))
n = 7
print(s.isHappy(n))
