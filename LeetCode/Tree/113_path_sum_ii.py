# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum): # mei xie chu lai
        """
        BFS + queque
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queque = [(root, root.val, [root.val])]
        while queque:
            node, val, ls = queque.pop(0)
            if not node.left and not node.right and targetSum == val:
                res.append(ls)
            if node.left:
                queque.append((node.left, val + node.left.val, ls + [node.left.val]))
            if node.right:
                queque.append((node.right, val + node.right.val, ls + [node.right.val]))
        return res


    def pathSum_DFS(self, root, targetSum): # mei xie chu lai
        """
        time O(n^2)
        space O(n)
        :param root:
        :param targetSum:
        :return:
        """
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root, targetSum, ls, res):
        if root:
            if not root.left and not root.right and root.val == targetSum:
                ls.append(root.val)
                res.append(ls)
            self.dfs(root.left, targetSum - root.val, ls + [root.val], res)
            self.dfs(root.right, targetSum - root.val, ls + [root.val], res)


    def pathSum_DFS_stack(self, root, targetSum): # mei xie chu lai
        """

        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return []
        res = []
        stack = [(root, targetSum - root.val, [root.val])]
        while stack:
            node, val, ls = stack.pop()
            if not node.left and not node.right and val == 0:
                res.append(ls)
            if node.right:
                stack.append((node.right, val - node.right.val, ls + [node.right.val]))
            if node.left:
                stack.append((node.left, val - node.left.val, ls + [node.left.val]))
        return res
