## 题目
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
## 用例
### Example:
```
Input:

   1
 /   \
2     3
 \
  5
```
Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

## 方法一
### 想法:
递归传参
```
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    result = []
    if root is not None:
        strn = str(root.val)
        self.search(root, strn, result)
    return result

    def search(self, root, strn, result):
        if root.left is None and root.right is None:
            result.append(strn)
        if root.left is not None:
            newstrn = strn + "->" + str(root.left.val)
            self.search(root.left, newstrn, result)
        if root.right is not None:
            newstrn = strn + "->" + str(root.right.val)
            self.search(root.right, newstrn, result)
```
