# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = new_node = ListNode(0)
        if head is None:
            return head
        if head.val == 0:
            new_node.next = head
            new_node = new_node.next
        while head:
            if head.val == new_node.val:
                head = head.next
            else:
                new_node.next = head
                new_node = new_node.next
                head = head.next
        # new_node.next = head_copy
        new_node.next = None
        return dummy.next

if __name__ == "__main__":
    solution = Solution()
    a = ListNode(1)
    a.next = ListNode(1)
    a = a.next
    a.next = ListNode(1)
    a = a.next
    a.next = ListNode(2)
    a = a.next
    a.next = ListNode(3)
    a = a.next
    a.next = ListNode(3)
    a = a.next
    a.next = ListNode(3)
    # a = a.next
    print(solution.deleteDuplicates(a))