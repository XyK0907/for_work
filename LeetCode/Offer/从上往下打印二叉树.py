"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
示例1
输入
{5,4,#,3,#,2,#,1}

返回值
[5,4,3,2,1]
"""

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return ans