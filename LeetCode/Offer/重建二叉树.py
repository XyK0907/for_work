"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,
6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
输入
[1,2,3,4,5,6,7],[3,2,4,1,6,5,7]

返回值
{1,2,5,3,4,6,7}
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            # 前序遍历中的第一个节点为根结点
            preorder_root = preorder_left
            # 在中序遍历中定位根结点
            inorder_root = index[pre[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(pre[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归的构造左子树， 并连接到根节点
            # 先序遍历中[从左边界+1开始的size_left_subtree]个元素就对应了中序遍历中[从左边界开始到根节点定位-1]的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root -1)
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)

            return root

        n = len(pre)
        index = {element: i for i, element in enumerate(tin)}
        return myBuildTree(0, n-1, 0, n-1)