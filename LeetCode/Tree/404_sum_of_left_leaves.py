class Solution(object):
    def sumOfLeftLeaves(self, root): #mei xie chu lai
        """
        time O(n)
        space O(n)
        :type root: TreeNode
        :rtype: int
        """
        isLeafNode = lambda node: not node.left and not node.right

        def dfs(node):
            ans = 0
            if node.left:
                ans += node.left.val if isLeafNode(node.left) else dfs(node.left)
            if node.right and not isLeafNode(node.right):
                ans += dfs(node.right)
            return ans
        return dfs(root) if root else 0

    def sumOfLeftLeaves_BFS(self, root): #mei xie chu lai
        """
        time O(n)
        space O(n)
        :param root:
        :return:
        """
        if not root:
            return 0
        isLeafNode = lambda node: not node.left and not node.right
        ans = 0
        queque = [(root)]
        while queque:
            node = queque.pop(0)
            if node.left:
                if isLeafNode(node.left):
                    ans += node.left.val
                else:
                    queque.append(node.left)
            if node.right:
                if not isLeafNode(node.right):
                    queque.append(node.right)
        return ans

