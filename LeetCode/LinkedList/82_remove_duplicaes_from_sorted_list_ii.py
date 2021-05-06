# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head): #mei xie chu lai
        """
        Time O(n)
        Space O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = newnode = ListNode(0)
        newnode.next = head
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                newnode.next = head.next
            else:
                newnode = newnode.next
            head = head.next
        return dummy.next

    def deleteDuplicates_recursive(self, head):
        """
        Time O(n)
        Space O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next != None and head.val == head.next.val:
            while head.next != None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head