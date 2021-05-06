# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head): # mei zuo chu lai
        """
        This can be solved by reversing the 2nd half and compare the two halves
        time O(n)
        space O(1)
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev


    def isPalindrome_1(self, head):
        """
        time O(n)
        Space O(n)
        :param head:
        :return:
        """
        vals = []
        while head:
            vals += head.val,
            head = head.next
        return vals == vals[::-1]

