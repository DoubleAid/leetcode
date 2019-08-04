###########################################################
# 19. Remove Nth Node From End of List
# 
# Description:
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
# Note:
# Given n will always be vali
#
# Solution:
# ���������Ҫ���ǵ����ҵ�����ν����滻������
# ��Ϊ���Ǻܿ���ɾ�����ǵ�һ��ͷ���
# ֻҪ������������ˣ������Ϳ�����
###########################################################
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        for i in range(1,n):
            p = p.next
        q = head
        n = None
        while p.next is not None:
            p = p.next
            n = q
            q = q.next
        if n is None:
            n = q.next
        else:
            n.next = q.next
            n = head
        return n
        