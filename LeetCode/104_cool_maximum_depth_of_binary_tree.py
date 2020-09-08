# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

    def maxDepth_BFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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

    def maxDepth_DFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        stack = [(root, 1)]
        while stack:
            root, leng = stack.pop()
            if not root:
                return 0

            if leng > depth:
                depth = leng

            if root.right:
                stack.append((root.right, leng + 1))
            if root.left:
                stack.append((root.left, leng + 1))
        return depth