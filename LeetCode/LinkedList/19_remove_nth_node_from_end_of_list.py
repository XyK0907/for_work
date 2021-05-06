# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        Time: O(L)
	    Space: O(1)
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if fast:
            slow.next = slow.next.next
        else:
            head = head.next
        return head

    def removeNthFromEnd_traverse(self, head, n):
        """
        Time: O(L)
        Space: O(1)
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def removeNthFromEnd_stack(self, head, n):
        """
        Time: O(L)
        Space: O(L)
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """