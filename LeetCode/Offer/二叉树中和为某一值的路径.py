"""
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
示例1
输入
{10,5,12,4,7},22

返回值
[[10,5,7],[10,12]]

示例2
输入
{10,5,12,4,7},15

返回值
[]
"""

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        ans = []
        queque = [(root, root.val, [root.val])]
        while queque:
            node, node_val, ls = queque.pop(0)
            if not node.left and not node.right and node_val == expectNumber:
                ans.append(ls)
            if node.left:
                queque.append([root.left, node_val + root.left.val, ls + [root.left.val]])
            if node.right:
                queque.append([root.right, node_val + root.right.val, ls + [root.right.val]])
        return ans


    def FindPath_DFS(self, root, expectNumber):
        ans = []
        self.dfs(root, expectNumber, [], ans)
        return ans

    def dfs(self, root, expectNumber, ls, ans):
        if root:
            if not root.left and not root.right and expectNumber == root.val:
                ls.append(root.val)
                ans.append(ls)
            self.dfs(root.left, expectNumber - root.val, ls + [root.val], ans)
            self.dfs(root.right, expectNumber - root.val, ls + [root.val], ans)