## 题目
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
## 用例
### Example 1:
```
Input:
11110
11010
11000
00000

Output: 1
```
### Example 2:
```
Input:
11000
11000
00100
00011

Output: 3
```
## 方法一
### 思路
深度优先便利
#### time 91.91% memory 83.02%
```
class Solution(object):
    def numIslands(self, grid):
        self.rowlen = len(grid)
        if self.rowlen == 0:
            return 0
        result = 0
        self.collen = len(grid[0])
        for i in range(self.rowlen):
            for j in range(self.collen):
                if grid[i][j] == "1":
                    self.sebrade([i,j],grid)
                    result += 1
        return result
    
    def sebrade(self,position,grid):
        i,j = position[0],position[1]
        grid[i][j] = 0
        if i > 0 and grid[i-1][j] == "1":
            self.sebrade([i-1,j],grid)
        if i < self.rowlen-1 and grid[i+1][j] == "1":
            self.sebrade([i+1,j],grid)
        if j > 0  and grid[i][j-1] == "1":
            self.sebrade([i,j-1],grid)
        if j < self.collen-1 and grid[i][j+1] == "1":
            self.sebrade([i,j+1],grid)
```
