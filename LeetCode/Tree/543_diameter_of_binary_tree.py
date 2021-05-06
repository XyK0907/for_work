# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        DFS
        time O(n)
        space O(height)
        :type root: TreeNode
        :rtype: int
        """
        self.max_length = 0
        def maxDepth(root):
            if not root:
                return 0
            left_branch = maxDepth(root.left)
            right_branch = maxDepth(root.right)
            self.max_length = max(self.max_length, left_branch + right_branch)
            return max(left_branch, right_branch) + 1
        maxDepth(root)
        return self.max_length