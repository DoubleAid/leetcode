###########################################################
#002 Add Two Number
#
#Introduce:
# You are given two non-empty linked lists representing two
#  non-negative integers. The digits are stored in reverse
#  order and each of their nodes contain a single digit. 
#  Add the two numbers and return it as a linked list.
#  You may assume the two numbers do not contain any leading
#  zero, except the number 0 itself.
#
#Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#Solution:
# 两种思路，第一种就是边读边写，第二种是读完再写
# 两者注意输入和输出时倒序的
# 
###########################################################

###########################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
###########################################################

'''方法一'''
class Solution:
    def NodeToInt(self,nodeli):
        '''
        :type nodeli:ListNode
        :return: int
        '''
        nlist = nodeli
        num = str(nlist.val)
        while nlist.next != None:
            nlist = nlist.next
            num = num+str(nlist.val)
        num = int(str(num)[::-1])
        return num

    def intToNode(self,num):
        '''
        :param num:the num
        :type num:int
        :return: ListNode
        '''
        numString = str(num)
        listnodes = None
        for i in range(0,len(numString)):
            li = ListNode(int(numString[i]))
            li.next = listnodes
            listnodes = li
        return listnodes

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0 and l1.next == None:
            return l2
        elif l2.val == 0 and l2.next == None:
            return l1
        num1=self.NodeToInt(l1)
        print(num1)
        num2=self.NodeToInt(l2)
        print(num2)
        ln = self.intToNode(num1+num2)
        return ln

'''方法二'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rest = 0
        head = None
        current = None
        while l1 is not None or l2 is not None or rest != 0 :
            if l1 is not None:
                rest += l1.val
                l1 = l1.next
            if l2 is not None:
                rest += l2.val
                l2 = l2.next
            li = ListNode(rest%10)
            rest = rest//10
            if head is not None:
                current.next = li
                current = current.next
            else:
                head = li
                current = li
        return head
