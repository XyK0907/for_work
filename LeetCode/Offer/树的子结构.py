"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构
输入
{8,8,#,9,#,2,#,5},{8,9,#,2}

返回值
true
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        return self.dfs(pRoot1, pRoot2)

    def dfs(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.check(pRoot1, pRoot2) or self.dfs(pRoot1.left, pRoot2) or self.dfs(pRoot1.right, pRoot2)

    def check(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1:
            return False
        if not pRoot2:
            return True
        if pRoot1.val != pRoot2.val:
            return False
        return self.check(pRoot1.left, pRoot2.left) and self.check(pRoot1.right, pRoot2.right)