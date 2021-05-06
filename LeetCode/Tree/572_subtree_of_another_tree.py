# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t): #mei xie chu lai
        """
        深度优先搜索暴力匹配
        深度优先搜索枚举 sss 中的每一个节点，判断这个点的子树是否和 ttt 相等。如何判断一个节点的子树是否和 ttt 相等呢，我们又需要做一次深度优
        先搜索来检查，即让两个指针一开始先指向该节点和 ttt 的根，然后「同步移动」两根指针来「同步遍历」这两棵树，判断对应位置是否相等
        Time O(s * t)
        space:假设 s 深度为 ds，t 的深度为 dt，任意时刻栈空间的最大使用代价是 O(max{ds,dt})O。故渐进空间复杂度为 O(max{ds,dt})

        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.dfs(s, t)

    def dfs(self, s, t):
        if not s:
            return False
        return self.check(s,t) or self.dfs(s.left, t) or self.dfs(s.right, t)

    def check(self, s, t):
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)


    def isSubtree_preorder(self, s, t): #mei xie chu lai
        """
        假设 s 由两个点组成，1 是根，2 是 1 的左孩子；t 也由两个点组成，1 是根，2 是 1 的右孩子。这样一来 s 和 t 的深度优先搜索序列相同，
        可是 t 并不是 s 的某一棵子树。由此可见「s 的深度优先搜索序列包含 t 的深度优先搜索序列」是「t 是 s 子树」的必要不充分条件，
        所以单纯这样做是不正确的。
        为了解决这个问题，我们可以引入两个空值 lNull 和 rNull，当一个节点的左孩子或者右孩子为空的时候，就插入这两个空值，这样深度优先搜索序列
        就唯一对应一棵树。处理完之后，就可以通过判断「s 的深度优先搜索序列包含 t 的深度优先搜索序列」来判断答案
        time O(m^2 + n^2 + m*n)
        space O(max(m, n))
        :param s:
        :param t:
        :return:
        """
        # trees = set()
        tree1 = self.preorder(s, True)
        tree2 = self.preorder(t, True)
        return tree2 in tree1

    def preorder(self, t, left):
        if not t:
            if left:
                return 'lnull'
            else:
                return 'rnull'
        return '#' + t.val + " " + self.preorder(t.left, True) + ' ' + self.preorder(t.right, False)

