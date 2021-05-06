# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        Recursion, DFS
        time O(n)
        space O(n)
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self,left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            outside = self.isMirror(left.left, right.right)
            inside = self.isMirror(left.right, right.left)
            return outside and inside
        return False

    def isSymmetric_iter(self, root):
        """
        iterative, BFS
        time O(n)
        space O(n)
        :param root:
        :return:
        """
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True






