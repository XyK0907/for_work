# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        方法一：自顶向下的递归
        time O(n^2)
        space O(n) 空间复杂度主要取决于递归调用的层数，递归调用的层数不会超过 n
        :type root: TreeNode
        :rtype: bool
        """
        def maxDepth(root):
            if not root:
                return 0
            left_branch = maxDepth(root.left) + 1
            right_brance = maxDepth(root.right) + 1
            return max(left_branch, right_brance)

        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(maxDepth(root.left) - maxDepth(root.right)) <= 1

    def isBalanced_1(self, root):
        """
        方法二：自底向上的递归
        自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。如果一棵子树
        是平衡的，则返回其高度（高度一定是非负整数），否则返回 −1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。
        time O(n)
        space O(n)
        :param root:
        :return:
        """
        def maxDepth(root):
            if not root:
                return 0
            left_branch = maxDepth(root.left)
            right_branch = maxDepth(root.right)
            if left_branch == -1 or right_branch == -1 or abs(left_branch - right_branch) > 1:
                return -1
            else:
                return max(left_branch, right_branch) + 1

        return maxDepth(root) >= 0
