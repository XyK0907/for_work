# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

    def recursive(self, array, start, end, last_treenode):
        if start > end:
            return -1
        if start == end:

            mid = start + (end - start) // 2
            new_node = TreeNode(mid)
            if not last_treenode.left:
                return self.recursive(array, start,mid-1,new_node)
            if not last_treenode.right:
                return self.recursive(array,mid + 1, end, new_node)

