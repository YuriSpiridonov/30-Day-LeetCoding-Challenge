"""
Task 9:
    Given two strings S and T, return if they are equal when both are typed 
    into empty text editors. # means a backspace character.

    Example 1:
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".
"""
#Difficulty: Easy
#104 / 104 test cases passed.
#Runtime: 24 ms
#Memory Usage: 14 MB

#Runtime: 24 ms, faster than 90.48% of Python3 online submissions for 
#Backspace String Compare.
#Memory Usage: 14 MB, less than 8.00% of Python3 online submissions for 
#Backspace String Compare.

import re

class Solution:
    #def backspaceCompare(self, S: str, T: str) -> bool:
    def backspaceCompare(S, T):
        S, T = S[::-1] , T[::-1] # reverse strings
        while '#' in S or '#' in T: # while "backspace used"
            S = re.sub(r'#{1}\w{1}|#$', '', S) # replace all '#l' patterns with nothing 
            T = re.sub(r'#{1}\w{1}|#$', '', T) # and clear last backspace symbol
        return bool(S == T)

#Tests
S = "ab#cb#cb#cb#c"
T = "ab#cb#cb#cb#c"
print(Solution.backspaceCompare(S, T), 'true')
S = "ab##"
T = "c#d#"
print(Solution.backspaceCompare(S, T), 'true')
S = "a#c"
T = "b"
print(Solution.backspaceCompare(S, T), 'false')
S = "xywrrmp"
T = "xywrrmu#p"
print(Solution.backspaceCompare(S, T), 'true')
S = "a##c"
T = "#a#c"
print(Solution.backspaceCompare(S, T), 'true')
S = "y#fo##f"
T = "y#f#o##f" 
