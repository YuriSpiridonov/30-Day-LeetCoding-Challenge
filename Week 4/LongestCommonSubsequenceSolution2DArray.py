"""
Task 26:
    Given two strings text1 and text2, return the length of their longest 
    common subsequence.
    A subsequence of a string is a new string generated from the original 
    string with some characters(can be none) deleted without changing the 
    relative order of the remaining characters. (eg, "ace" is a subsequence 
    of "abcde" while "aec" is not). A common subsequence of two strings is 
    a subsequence that is common to both strings.
    If there is no common subsequence, return 0.
    
    Theory: https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
"""
#37 / 37 test cases passed.
#Runtime: 512 ms
#Memory Usage: 21.5 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = len(text1)
        y = len(text2)
        array = [ [0] * (y + 1) for _ in range(x + 1) ]
        for row in range(x + 1):
            for col in range(y + 1):
                if row == 0 or col == 0: array[row][col] = 0
                elif text1[row - 1] == text2[col - 1]: array[row][col] = array[row - 1][col - 1] + 1
                else: array[row][col] = max(array[row - 1][col],array[row][col - 1])
        return array[x][y]
