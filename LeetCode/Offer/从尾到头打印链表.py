"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

示例1
输入
{67,0,24,58}

返回值
[58,24,0,67]
"""

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]

    def printListFromTailToHead_stack(self, listNode):
        """
        time O(n)
        space O(n)
        :param listNode:
        :return:
        """
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans

    def printListFromTailToHead_recursion(self, listNode):
        """
        time O(n)
        space O(n)
        :param listNode:
        :return:
        """
        return self.printListFromTailToHead_recursion(listNode.next) + [listNode.val] if listNode else []