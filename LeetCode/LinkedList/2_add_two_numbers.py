# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        time O(max(m,n) + 1)
        space O(max(m,n) + 1)
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = new_node = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            new_node.next = ListNode(carry % 10)
            new_node = new_node.next
            carry = carry // 10
        return dummy.next