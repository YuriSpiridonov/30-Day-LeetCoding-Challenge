"""
Task 17:
    Given a 2d grid map of '1's (land) and '0's (water), count the number of 
    islands. An island is surrounded by water and is formed by connecting 
    adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    
    Example:
    Input:
    
    11000
    11000
    00100
    00011
    
    Output: 3
    
    Approach and algorithm here:
    https://www.youtube.com/watch?v=WRxGI8TeckU 
"""
#Difficulty: Medium
#47 / 47 test cases passed.
#Runtime: 156 ms
#Memory Usage: 14.9 MB

class Solution:
    #def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(grid):
        numberOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    numberOfIslands += 1
                    Solution.dfs(grid, i, j)
        return numberOfIslands
                    
    def dfs(grid, row, col):
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[row]) - 1 or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        Solution.dfs(grid, row, col - 1)
        Solution.dfs(grid, row - 1, col)
        Solution.dfs(grid, row, col + 1)
        Solution.dfs(grid, row + 1, col)
      
#Tests
grid = [["1","1","0","0","0"],
        ["1","1","0","1","1"],
        ["0","0","1","0","0"],
        ["1","1","0","1","1"]]
print(Solution.numIslands(grid), '5')
grid = [["1","0","1","0","1"],
        ["0","1","0","1","0"],
        ["1","0","1","0","1"],
        ["0","1","0","1","0"]]
print(Solution.numIslands(grid), '10')
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
print(Solution.numIslands(grid), '1')
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
print(Solution.numIslands(grid), '3')
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["1","1","1","1","1"]]
print(Solution.numIslands(grid), '2')
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","0","1","0"],
        ["1","1","1","1","1"]]
print(Solution.numIslands(grid), '2')
grid = [["1","1","0","0","0"],
        ["1","1","0","1","1"],
        ["0","0","0","0","0"],
        ["1","1","0","1","1"]]
print(Solution.numIslands(grid), '4')
grid = [["1","1","0","0","0"],
        ["1","1","0","1","1"],
        ["0","0","1","0","0"],
        ["1","1","0","1","1"]]
print(Solution.numIslands(grid), '5')
