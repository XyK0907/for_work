"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
--> 142. linked_list_cycle_II.py
"""

class Solution:
    def EntryNodeOfLoop(self, head):
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