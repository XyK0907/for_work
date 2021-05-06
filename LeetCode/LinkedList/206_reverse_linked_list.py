# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        dic = {}
        i = 0
        while head:
            dic[i] = head
            head = head.next
            i += 1
        dummy = cur = dic[i-1]
        i = i -1
        while i >= 1:
            cur.next = dic[i-1]
            cur = cur.next
            i -= 1
        cur.next = None
        return dummy

    def reverseList_iter(self, head):
        """
        time O(n)
        space O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList_recursion(self, head):
        if head is None or head.next is None:
            return head
        p = self.reverseList_recursion(head.next)
        head.next.next = head
        head.next = None
        return p