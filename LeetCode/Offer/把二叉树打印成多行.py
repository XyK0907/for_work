"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
示例1
输入
{8,6,10,5,7,9,11}

返回值
[[8],[6,10],[5,7,9,11]]
"""

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        ans = []
        queque = [pRoot]
        while queque:
            value = []
            length = len(queque)
            for _ in range(length):
                node = queque.pop(0)
                value.append(node.val)
                if node.left:
                    queque.append(node.left)
                if node.right:
                    queque.append(node.right)
            ans.append(value)
        return ans