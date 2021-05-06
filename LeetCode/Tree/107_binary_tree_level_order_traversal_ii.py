# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        res = [[root.val]]
        while level:
            queque = []
            value = []
            for el in level:
                if el.left:
                    queque.append(el.left)
                    value.append(el.left.val)
                if el.right:
                    queque.append(el.right)
                    value.append(el.right.val)
            if value:
                res.append(value)
            level = queque
        return res[::-1]

    def levelOrderBottom_bfs(self, root):
        """
        time O(n)
        space O(n)
        :param root:
        :return:
        """
        import collections
        level = []
        if not root:
            return level
        q = collections.deque([root])
        while q:
            value = list()
            for _ in q:
                node = q.popleft()
                value.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level.append(value)
        return level[::-1]


    def levelOrderBottom1(self, root):
        res = []
        self.dfs(root, 0, res)
        return res


    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level + 1)].append(root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)


    # dfs + stack
    def levelOrderBottom2(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res


