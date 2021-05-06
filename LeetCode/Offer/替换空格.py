"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

"""

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.replace(' ', '%20')

    def replaceSpace_(self, s):
        """
        time O(n)
        space O(n)
        :param s:
        :return:
        """
        res = []
        for c in s:
            if c == ' ':
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)


'''
方法二：这一题的关键是替换是从往后往前遍历还是从前往后遍历是不一样的，如果从前往后遍历的话，每一个空格都要移动这个空格后面
所有的字符串一次，但是如果从后往前遍历的话，每一个字符串只需要移动一次。
'''