# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        iteratively
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNodef
        """
        dummy = new_node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                new_node.next = l1
                l1 = l1.next
            else:
                new_node.next = l2
                l2 = l2.next
            new_node = new_node.next

        new_node.next = l1 or l2
        return dummy.next


    def mergeTwoLists_recursive(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNodef
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


l1 = ListNode(1)
l1.next = a = ListNode(2)
a.next = ListNode(4)

l2 = ListNode(1)
l2.next = b = ListNode(3)
b.next = ListNode(4)

solution = Solution()
print(solution.mergeTwoLists(l1, l2))





