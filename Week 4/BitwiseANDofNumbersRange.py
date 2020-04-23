"""
Task 23:
    Given a range [m, n] where 0 <= m <= n <= 2147483647, return 
    the bitwise AND of all numbers in this range, inclusive.

    Example:
    Input: [5,7]
    Output: 4
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        c = 0
        while m != n:
            m >>= 1
            n >>= 1
            c+=1
        return m << c
