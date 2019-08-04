# 题目
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# 例子
## Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

## Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

## Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

## 方法一
### 想法:
使用两个指针，一个快一个慢，如果快指针遇到了 None，说明该数组没有循环
如果在某一时刻快指针和慢指针相遇了，说明链表中存在环
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while True:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
```
