"""
Task 16:
    Given a string containing only three types of characters: '(', ')' and '*',
    write a function to check whether this string is valid. 
    We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or 
    a single left parenthesis '(' or an empty string.
    An empty string is also valid.
"""
# Not complete

class Solution:
    #def checkValidString(self, s: str) -> bool:
    def checkValidString(s):
        while '()' in s:
            s = s.replace('()', '')
        if len(s) > 2 and (s[-1] == '(' or s[0] == ')'): return False
        s = s.replace(')(', ') (')
        l = s.split(' ')
        for i in range(len(l)):
            if '*' in l[i]:
                c = l[i].count('(')-l[i].count(')')
                if c != 0:
                    if l[i].count('*') >= abs(c):
                        l[i] = True
                    else:
                        l[i] = False
                else:
                    l[i] = True
            elif l[i].count('(')-l[i].count(')') == 0:
                l[i] = True
            else:
                l[i] = False  
        return True if False not in l else False
        
#Tests
s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()" # True
print(Solution.checkValidString(s),'true') 
s = "(*()()())(((*(()((((()())()()*()(())))))(((*(()*)())((())))(((()))))*)))((()())(*())**((())))(*)"
print(Solution.checkValidString(s),'true') # failing this one
