## 题目
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
## 用例
### Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
#### Note:

Assume that the total area is never beyond the maximum possible value of int.

## 方法一
### 思路
两个面积相加，剪掉重复的部分
#### time 50% memory 了12.5%
```
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        X = abs(A-C)*abs(B-D)
        Y = abs(E-G)*abs(F-H)
        maxx = max(A,E)
        maxy = max(B,F)
        minx = min(C,G)
        miny = min(H,D)
        if maxx > minx or maxy > miny:
            return X+Y
        return X+Y-abs(maxx-minx)*abs(maxy-miny)
```
