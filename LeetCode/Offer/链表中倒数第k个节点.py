"""
输入一个链表，输出该链表中倒数第k个结点。
示例1
输入
1,{1,2,3,4,5}

返回值
{5}
"""
class Solution:
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return None
        slow = fast = head
        for i in range(k):
            if fast:
                fast = fast.next
            else:
                return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow