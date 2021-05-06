# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum): #mei xie chu lai
        """
        Brute Force
        time:
            Time complexity depends on the two DFS.
            1st layer DFS will always take O(n), due to here we will take each node out, there are in total n TreeNodes
            2nd layer DFS will take range from O(n) (single sided tree) to O(logn)(balanced tree). This is due to here
            we are get all the paths from a given node. The length of path is proportional to the tree height.
            Therefore, the total time complexity is O(nlogn) to O(n^2).
        space:
            Space complexity is O(1), due to there is no extra cache. However, for any recursive question, we need to
            think about stack overflow, namely the recursion should not go too deep.
            Assume we have n TreeNodes in total, the tree height will vary from O(n) (single sided tree) to O(logn)
            (balanced tree).
            The two DFS will go as deep as the tree height.
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.numOfPath = 0
        # 1st layer DFS to go through each node
        self.dfs(root, sum)
        return self.numOfPath

    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        if not node:
            return
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if not node:
            return
        if node.val == target:
            self.numOfPath += 1
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)

    def pathSum_prefixsum(self, root, sum): #mei xie chu lai
        """
        In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the
        intermediate result. Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5,
         we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.

        This is a classical 'space and time tradeoff': we can create a dictionary (named cache) which saves all the path
         sum (from root to current node) and their frequency.

        Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If
        within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.

        We just need to add the frequency of the oldPathSum to the result.

        During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.

        time O(n) as we just traverse once
        space O(n) extra space
        :param root:
        :param sum:
        :return:
        """
        self.result = 0
        cache = {0:1}
        self.dfs(root, sum, 0, cache)
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if not root:
            return

        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target

        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1



