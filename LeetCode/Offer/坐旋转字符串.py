"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

限制：

    1 <= k < s.length <= 10000


"""

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        list method
        time O(n)
        space O(n)
        :type s: str
        :type n: int
        :rtype: str
        """
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return  ''.join(res)

    def reverseLeftWords_slice(self, s, n):
        """
        time O(n)
        space O(n)
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]