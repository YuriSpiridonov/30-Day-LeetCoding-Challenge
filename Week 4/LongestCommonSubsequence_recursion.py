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
    
    Theory: https://www.youtube.com/watch?v=ASoaQq66foQ
"""
#Status: Time Limit Exceeded

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0: return 0
        i = len(text1)-1
        j = len(text2)-1
        if text1[i] == text2[j]: return 1 + Solution.longestCommonSubsequence(text1[:i], text2[:j])
        else: return max(Solution.longestCommonSubsequence(text1, text2[:j]), Solution.longestCommonSubsequence(text1[:i], text2))
