# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        time O(n^2)
        space O(n^2)
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        queque = [(root, str(root.val))]
        while queque:
            node, ls = queque.pop(0)
            if not node.left and not node.right:
                res.append(ls)
            if node.left:
                queque.append((node.left, ls + '->' + str(node.left.val)))
            if node.right:
                queque.append((node.right, ls + '->' + str(node.right.val)))
        return res

    def binaryTreePaths_DFS(self, root):
        def constrcut_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    constrcut_paths(root.left, path)
                    constrcut_paths(root.right, path)

        paths = []
        constrcut_paths(root, '')
        return paths


    def binaryTreePaths_DFS_stack(self, root):
        if not root:
            return []
        res = []
        stack = [(root, str(root.val))]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls)
            if node.right:
                stack.append((node.right, ls + '->' + str(node.right.val)))
            if node.left:
                stack.append((node.left, ls + '->' + str(node.left.val)))
        return res