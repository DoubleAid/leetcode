## 题目

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

## 用例
####Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

####Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
## 方法一
### 想法
1.复制给定链表的每一个节点，将其插入到给定链表中原节点的后面
2.复制random指针，由于新节点就在原节点的后面，因此，依次检测给定链表中的每一个节点，若random不为空，则将它的下一个节点的random指针指向原节点random指针所指节点的下一个节点
3.将该链表拆分成新旧两个链表，返回新链表
```
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        start = head
        if start is None:
            return None
        while start is not None:
            newNode = Node(start.val,start.next,None)
            start.next = newNode
            start = newNode.next
        start = head
        while start is not None:
            if start.random is not None:
                start.next.random = start.random.next
            start = start.next.next
        start = head
        newhead = start.next
        while start is not None:
            temp = start.next
            start.next = start.next.next
            if temp.next is not None:
                temp.next = temp.next.next
                start = start.next
            else:
                return newhead
```
