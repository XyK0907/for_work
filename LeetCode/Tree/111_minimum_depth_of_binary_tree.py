# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root): #mei xie chu lai
        """
        方法一：深度优先搜索
        首先可以想到使用深度优先搜索的方法，遍历整棵树，记录最小深度。
        对于每一个非叶子节点，我们只需要分别计算其左右子树的最小叶子节点深度。这样就将一个大问题转化为了小问题，可以递归地解决该问题。

        Time O(n)
        space O(logN) or O(n)
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1


    def minDepth_bfs(self, root): #mei xie chu lai
        """
        当我们找到一个叶子节点时，直接返回这个叶子节点的深度。广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小

        time O(n)
        space O(n) 其中 N 是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数
        :param root:
        :return:
        """
        import collections
        if not root:
            return 0

        queque = collections.deque([(root, 1)])
        while queque:
            node, depth = queque.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queque.append((node.left, depth + 1))
            if node.right:
                queque.append((node.right, depth + 1))

        return 0


    def minDepth_1(self, root): #mei xie chu lai
        """
        We need to add the smaller one of the child depths - except if that's zero, then add the larger one.
        :param root:
        :return:
        """
        if not root: return 0
        d = list(map(self.minDepth_1, (root.left, root.right)))
        return 1 + (min(d) or max(d))

        # if root == None:
        #     return 0
        # if root.left == None or root.right == None:
        #     return self.minDepth(root.left) + self.minDepth(root.right) + 1
        # return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
