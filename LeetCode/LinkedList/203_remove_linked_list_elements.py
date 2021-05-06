# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        time O(n)
        space O(1)
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        while head:
            if head.val != val:
                prev.next = head
                head = head.next
                prev = prev.next
            else:
                prev.next = head.next
                head = head.next
        return dummy.next

    def removeElements_recursive(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        head.next = self.removeElements_recursive(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head