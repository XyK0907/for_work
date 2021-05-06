# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees_DFS(self, root1, root2): #mei xie chu lai
        """
        time O(min(M, N))
        space O(min(m, n))
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        if not root2:
            return root1
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged

    def mergeTrees_BFS(self, root1, root2): #mei xie chu lai
        """

        :param root1:
        :param root2:
        :return:
        """
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        queque = [(root1, root2, merged)]
        while queque:
            node1, node2, new = queque.pop(0)
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    new.left = left
                    queque.append((left1, left2, left))
                elif left1:
                    new.left = left1
                elif left2:
                    new.left = left2
            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    new.right = right
                    queque.append((right1, right2, right))
                elif right1:
                    new.right = right1
                elif right2:
                    new.right = right2
        return merged

