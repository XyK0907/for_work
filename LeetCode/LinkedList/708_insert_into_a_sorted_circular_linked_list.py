"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal): #mei xie chu lai
        """
        ascending order
        time O(n)
        space O(1)
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            head = ListNode(insertVal)
            head.next = head
            return head

        p, c = head, head.next
        while True:
            if p.val <= insertVal <= c.val:
                p.next = ListNode(insertVal, c)
                break
            if p.val > c.val:
                if p.val <= insertVal or insertVal <= c.val:
                    p.next = ListNode(insertVal, c)
                    break
            p = p.next
            c = c.next
            if p == head:
                p.next = ListNode(insertVal, c)
                break
        return head
