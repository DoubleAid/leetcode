# 题目
Given a binary tree, return the preorder traversal of its nodes' values.
# 用例
## Example 1:

Input: [1,null,2,3]
   1  
    \  
     2  
    /  
   3  

Output: [1,2,3]

## 方法一
### 想法:
利用堆栈保存相应的信息
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        temp = [root]
        result = []
        while temp:
            node = temp.pop()
            result.append(node.val)
            if node.right is not None:
                temp.append(node.right)
            if node.left is not None:
                temp.append(node.left)
        return result
```
