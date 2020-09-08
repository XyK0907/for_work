# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_branch = self.maxDepth(root.left) + 1
        right_branch = self.maxDepth(root.right) + 1
        return max(left_branch,right_branch)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is None and root.right is None:
            return 0
        diameter = self.maxDepth(root.left) + self.maxDepth(root.right) + 2
        diameter_left = self.diameterOfBinaryTree(root.left)
        diameter_right = self.diameterOfBinaryTree(root.right)
        return max(diameter, diameter_left, diameter_right)