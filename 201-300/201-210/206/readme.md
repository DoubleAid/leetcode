## 题目
Reverse a singly linked list.
## 用例
### Example:
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
#### Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

## 方法一
### 想法:
利用栈倒换位置
#### time 63.47% memory 34.18%
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
def reverseList(self, head):
"""
:type head: ListNode
:rtype: ListNode
"""
stack = []
while head is not None:
stack.append(head)
head = head.next
newhead = ListNode(1)
p = newhead
while stack:
node = stack.pop()
p.next = node
p = p.next
p.next = None
return newhead.next
```
