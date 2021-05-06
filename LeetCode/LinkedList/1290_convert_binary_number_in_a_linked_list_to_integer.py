# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return int(''.join(str(e) for e in res), base=2)

    def getDecimalValue1(self, head):
        """
        Binary Representation
        time O(n)
        space O(1)
        :type head: ListNode
        :rtype: int
        """
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num

    def getDecimalValue2(self, head):
        """
        Bit Manipulation
        time O(n)
        space O(1)
        :type head: ListNode
        :rtype: int
        """
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val
            head = head.next
        return num