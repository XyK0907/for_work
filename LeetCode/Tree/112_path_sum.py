# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
注意到本题的要求是，询问是否有从「根节点」到某个「叶子节点」经过的路径上的节点之和等于目标和。核心思想是对树进行一次遍历，在遍历时记录从根节点到当
前节点的路径和，以防止重复计算.

"""
class Solution(object):
    def hasPathSum_BFS(self, root, targetSum): #mei xie chu lai
        """
        记录从根节点到当前节点的路径和，以防止重复计算。这样我们使用两个队列，分别存储将要遍历的节点，以及根节点到这些节点的路径和即可。
        time O(n)
        space O(n)
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        import collections
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])

        while que_node:
            node = que_node.popleft()
            temp = que_val.popleft()
            if not node.left and not node.right:
                if temp == targetSum:
                    return True
                continue

            if node.left:
                que_node.append(node.left)
                que_val.append(node.left.val + temp)
            if node.right:
                que_node.append(node.right)
                que_val.append(node.right.val + temp)

        return False

    def hasPathSum_stack(self, root, targetSum): #mei xie chu lai
        """
        除了上面的 队列 解法以外，也可以使用 栈，同时保存节点和到这个节点的路径和。但是这个解法已经不是 BFS。因为会优先访问 后进来 的节点，导致
        会把根节点的右子树访问结束之后，才访问左子树。

        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, temp = stack.pop()
            if not node.left and not node.right and targetSum == temp:
                return True
            if node.left:
                stack.append((node.left, temp + node.left.val))
            if node.right:
                stack.append((node.right, temp + node.right.val))
        return False

    def hasPathSum_recursion(self, root, targetSum): #mei xie chu lai
        """
        DFS
        是否存在从当前节点的子节点到叶子的路径，满足其路径和为 sum - val
        不难发现这满足递归的性质，若当前节点就是叶子节点，那么我们直接判断 sum 是否等于 val 即可（因为路径和已经确定，就是当前节点的值，我们只
        需要判断该路径和是否满足条件）。若当前节点不是叶子节点，我们只需要递归地询问它的子节点是否能满足条件即可
        time O(n)
        space O(logn) or O(n)
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum_recursion(root.left, targetSum - root.val) or \
               self.hasPathSum_recursion(root.right, targetSum - root.val)

    def hasPathSum_backtracking(self, root, targetSum): #mei xie chu lai
        """
        这里的回溯指 利用 DFS 找出从根节点到叶子节点的所有路径，只要有任意一条路径的 和 等于 sum，就返回 True
        下面的代码并非是严格意义上的回溯法，因为没有重复利用 path 变量
        :param root:
        :param targetSum:
        :return:
        """
        if not root: return False
        res = []
        return self.dfs(root, targetSum, res, [root.val])

    def dfs(self, root, target, res, path):
        if not root: return False
        if sum(path) == target and not root.left and not root.right:
            return True
        left_flag, right_flag = False, False
        if root.left:
            left_flag = self.dfs(root.left, target, res, path + [root.left.val])
        if root.right:
            right_flag = self.dfs(root.right, target, res, path + [root.right.val])
        return left_flag or right_flag

