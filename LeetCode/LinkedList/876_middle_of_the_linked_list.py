# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        time O(n)
        space O(n)
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        i = 0
        while head:
            dic[i] = head.val
            head = head.next
            i += 1
        return dic[i // 2]

    def middleNode_slow_fast(self, head):
        """
        When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast.
        When fast reaches the end of the list, slow must be in the middle.
        time O(n)
        space O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow