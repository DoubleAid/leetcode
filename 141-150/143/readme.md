## 题目
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
## 用例
### Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
### Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
## 方法一
### 想法
将整个链表压入栈内，依次各从上下弹出元素连接
#### time 20%
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        flag = True
        headnode = ListNode(0)
        p = headnode
        while stack:
            if flag:
                temp = stack.pop(0)
                flag = False
            else:
                temp = stack.pop()
                flag = True
            p.next = temp
            p = p.next
        p.next = None
        return headnode.next
```
## 方法二
### 想法
通过快慢指针确定中间位置，将之后的元素压入栈内，这会节省一半的空间和时间
### time 63% momery 5%
```
class Solution:
    def reorderList(self, head: ListNode) -> None:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        try:
            lastpart = slow.next
            slow.next = None
        except:
            lastpart = None
        stack = []
        while lastpart is not None:
            stack.append(lastpart)
            lastpart = lastpart.next
        fast = head
        while stack:
            temp = stack.pop()
            fast.next,temp.next = temp,fast.next
            fast = fast.next.next
```

