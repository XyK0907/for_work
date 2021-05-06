# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        my method
        time O(max(m, n))
        space O(1)
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum1, sum2 = 0, 0
        while l1:
            sum1 = sum1 * 10 + l1.val
            l1 = l1.next
        while l2:
            sum2 = sum2 * 10 + l2.val
            l2 = l2.next
        sum_all = sum1 + sum2

        head = ListNode(0)
        if sum_all == 0:
            return head
        while sum_all:
            v, sum_all = sum_all % 10, sum_all // 10
            head.next, head.next.next = ListNode(v), head.next
        return head.next

    def addTwoNumbers_stack(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        ans = None
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            newnode= ListNode(carry % 10)
            newnode.next = ans
            ans = newnode
            carry = carry // 10
        return ans