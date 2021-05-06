# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        iterative
        Time: O(n)
        Space: O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = newnode = ListNode(0)
        dummy.next = head
        while head and head.next:
            newnode.next = head.next
            head.next = head.next.next
            newnode.next.next = head
            head = head.next
            newnode = newnode.next.next
        return dummy.next

    def swapPairs_recursive(self, head):
        """
        Time: O(n)
        Space: O(n)
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        return newhead





