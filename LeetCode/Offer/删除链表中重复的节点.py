"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

示例1
输入
{1,2,3,3,4,4,5}

返回值
{1,2,5}
"""
class Solution:
    def deleteDuplication(self, pHead):
        dummy = newnode = ListNode(0)
        newnode.next = pHead
        while pHead:
            if pHead.next and pHead.val == pHead.next.val:
                while pHead.next and pHead.next.val == pHead.val:
                    pHead = pHead.next
                newnode.next = pHead.next
            else:
                newnode = newnode.next
            pHead = pHead.next
        return dummy.next

