"""
Task 6:
    Given an array of strings, group anagrams together.

    Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [["ate","eat","tea"],["nat","tan"],["bat"]]
    Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""

class Solution:
    #def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(strs):
        d= dict()
        for anagram in strs:
            s= ''.join(sorted(anagram))
            if s not in d.keys(): d[s] = [anagram]
            else: d[s].append(anagram)       
        return d.values()

#Tests        
array = ["eat", "tea", "tan", "ate", "nat", "bat"] 
print(Solution.groupAnagrams(array))
array = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
print(Solution.groupAnagrams(array))
array = ["ray","cod","abe","ned","arc","jar","owl","pop","paw","sky","yup","fed","jul","woo","ado","why","ben","mys","den","dem","fat","you","eon","sui","oct","asp","ago","lea","sow","hus","fee","yup","eve","red","flo","ids","tic","pup","hag","ito","zoo"]
print(Solution.groupAnagrams(array)) 
