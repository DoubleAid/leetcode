## 题目
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 
## 用例
### Example:
```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
```

#### Note:

+ next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
+ You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
## 方法一
### 思路
看到他的要求 O(1) time O(h）空间，第一个想到的就是把树转换成数组，这样只要O(1)时间就可以返回了，但是这样应该是不符合规范的
#### time 36.70% memory 97.73%
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        self.nodeval = []
        if root is None:
            return
        temp = [root]
        while temp:
            node = temp.pop()
            if node.right is not None:
                temp.append(node.right)
                node.right = None
            if node.left is not None:
                tempval = node.left
                node.left = None
                temp.append(node)
                temp.append(tempval)
                continue
            self.nodeval.append(node.val)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.nodeval.pop(0)
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.nodeval:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
