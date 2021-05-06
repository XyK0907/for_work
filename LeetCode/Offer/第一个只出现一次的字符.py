"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ' '
        dic = {}
        for each in s:
            dic[each] = dic.get(each, 0) + 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return ' '




if __name__ == '__main__':
    solution = Solution()
    print(solution.firstUniqChar('google'))