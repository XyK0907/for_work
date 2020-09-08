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
        output_list = [[root.val]]
        line = [root]
        while line:
            queue = []
            queue_val = []
            for element in line:
                if element.left:
                    queue.append(element.left)
                    queue_val.append(element.left.val)
                if element.right:
                    queue.append(element.right)
                    queue_val.append(element.right.val)
            line = queue
            output_list.append(queue_val)
        output_list.pop()
        return output_list[::-1]

