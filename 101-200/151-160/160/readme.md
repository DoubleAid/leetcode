## 题目

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 
## 用例
### Example 1:

```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the
                   two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From 
                   the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the 
                   intersected node in A; There are 3 nodes before the intersected node in B.
```

### Example 2:
```
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two 
                    lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the 
                    head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A;
                    There are 1 node before the intersected node in B.
```

## 方法一
### 想法
两个链表的尾巴相同，肯定要从尾巴进行比较，使用栈进行从后往前比较
#### time 63.81% memory 18.52%
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        Alist = []
        while headA is not None:
            Alist.append(headA)
            headA = headA.next
        Blist = []
        while headB is not None:
            Blist.append(headB)
            headB = headB.next
        A = None
        while Alist and Blist:
            A = Alist.pop()
            B = Blist.pop()
            if A != B:
                return A.next
        return A
```
