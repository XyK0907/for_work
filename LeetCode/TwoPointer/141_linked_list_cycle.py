# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Time; O(n)
        Space: O(n)
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        while head:
            if head not in dic:
                dic[head] = True
                head = head.next
            else:
                return True
        return False


    def hasCycle_cool(self, head):
        """
        Imagine two runners running on a track at different speed. What happens when the track is actually a circle?
        Time; O(n)
        Space: O(1)
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True