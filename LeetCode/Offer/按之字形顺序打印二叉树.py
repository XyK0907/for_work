"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
示例1
输入
{8,6,10,5,7,9,11}

返回值
[[8],[10,6],[5,7,9,11]]
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        queque = [pRoot]
        ans = []
        i = 0
        while queque:
            value = []
            length = len(queque)
            for _ in range(length):
                node = queque.pop(0)
                value.append(node.val)
                if node.left:
                    queque.append(node.left)
                if node.right:
                    queque.append(node.right)
            if i % 2 == 0:
                ans.append(value)
            else:
                ans.append(value[::-1])
            i += 1
        return ans