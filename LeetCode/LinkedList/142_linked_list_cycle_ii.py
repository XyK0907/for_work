# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        my solution: HashMap
        time: O(N)
        space: O(N)
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        while head not in seen:
            if head is None:
                return head
            seen.add(head)
            head = head.next
        return head

    def detectCycle_two_pointers(self, head):
        """
        slow and fast pointers

        time: O(N)
        space: O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head