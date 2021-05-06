"""
请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
示例1
输入
{8,6,6,5,7,7,5}

返回值
true

示例2
输入
{8,6,9,5,7,7,5}

返回值
false
"""

class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.isMirror(pRoot.left, pRoot.right)

    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        outside = self.isMirror(left.left, right.right)
        inside = self.isMirror(left.right, right.left)
        return outside and inside
