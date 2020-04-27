"""
Task 27:
    Given a 2D binary matrix filled with 0's and 1's, find the largest square 
    containing only 1's and return its area.

    Example:
    Input: 
    
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    
    Output: 4
"""
#Difficulty: Medium
#69 / 69 test cases passed.
#Runtime: 232 ms
#Memory Usage: 16.9 MB

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        x = len(matrix)
        y = len(matrix[0])
        matrix.append(["0"]*y)
        square = 0
        if x > 1:
            for row in range(x+1):
                matrix[row].append("0")
                for col in range(y+1):
                    if matrix[row][col] == '1': 
                        matrix[row][col] = str(1 + int(min(int(matrix[row-1][col]), int(matrix[row][col-1]), int(matrix[row-1][col-1]))))
                    if int(matrix[row][col]) > square: 
                        square = int(matrix[row][col])
        else: return max(matrix[0])
        return square*square
