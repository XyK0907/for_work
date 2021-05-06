# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k): #mei xie chu lai
        """
        Time O(n)
        Space O(1)
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(head, tail):
            prev = tail.next
            p = head
            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex
            return tail, head

        hair = ListNode(0)
        hair.next = head
        pre = hair
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = nex
        return hair.next

    def reverseKGroup_iter1(self, head, k): #mei xie chu lai
        """
        Time O(n)
        Space O(1)
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)


    def reverseKGroup_recursion(self, head, k): #mei xie chu lai
        """
        Time O(n)
        Space O(1)
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        node, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return node