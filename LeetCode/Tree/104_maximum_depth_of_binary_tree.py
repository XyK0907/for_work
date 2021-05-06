# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    def maxDepth_iter_bfs(self, root):
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
        return depth

    def maxDepth_iter_dfs(self, root):
        depth = 0
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if not node:
                depth = max(depth, level)
            else:
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        return depth





