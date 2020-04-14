"""
Task 14:
    You are given a string s containing lowercase English letters, 
    and a matrix shift, where shift[i] = [direction, amount]:
        1. direction can be 0 (for left shift) or 1 (for right shift). 
        2. amount is the amount by which string s is to be shifted.
        3. A left shift by 1 means remove the first character of s and 
           append it to the end.
        4. Similarly, a right shift by 1 means remove the last character of s 
           and add it to the beginning.
    Return the final string after all operations.
    
    Example 2:
    Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
    Output: "efgabcd"
    Explanation:  
    [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
    [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
    [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
    [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
"""
#31 / 31 test cases passed.
#Runtime: 36 ms
#Memory Usage: 14 MB

class Solution:
    #def stringShift(self, s: str, shift: List[List[int]]) -> str:
    def stringShift(s, shift):
        for shifter in shift:
            if shifter[0] == 0: s = s[shifter[1]:]+s[:shifter[1]]
            else: s = s[-shifter[1]:]+s[:-shifter[1]]
        return s
    
#Tests
s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]
print(Solution.stringShift(s, shift), "efgabcd")
