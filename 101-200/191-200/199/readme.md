## 题目
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
## 用例
### Example:
```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```
## 方法一
### 思路
一层一层，按层遍历
#### time 86.66% memory 40.36%
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        result = []
        temp = []
        if root is not None:
            temp = [root]
        while temp:
            linelen = len(temp)
            result.append(temp[0].val)
            for i in range(linelen):
                node = temp.pop(0)
                if node.right is not None:
                    temp.append(node.right)
                if node.left is not None:
                    temp.append(node.left)
        return result
```
