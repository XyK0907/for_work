"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
示例1
输入
{1,3,5},{2,4,6}

返回值
{1,2,3,4,5,6}
"""

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        dummy = newnode = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                newnode.next = pHead1
                pHead1 = pHead1.next
            else:
                newnode.next = pHead2
                pHead2 = pHead2.next
            newnode = newnode.next

        if pHead1:
            newnode.next = pHead1
        elif pHead2:
            newnode.next = pHead2
        return dummy.next