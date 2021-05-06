"""
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
返回值描述:
如果是合法的数值表达则返回该数字，否则返回0

示例1
输入
"+2147483647"
返回值
2147483647

示例2
输入
"1a33"
返回值
0
"""

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        """
        time O(n)
        space O(n)
        :param s:
        :return:
        """
        s = s.strip()  #O(n) space
        if not s: return 0
        minus = False
        i = 1
        if s[0] == '-':
            minus = True
        elif s[0] != '+':
            i = 0
        ans = 0
        for c in s[i:]:
            if not c.isdigit():
                return 0
            else:
                ans = ans * 10 + ord(c) - ord('0')
        if minus:
            ans = -ans
        return ans




if __name__ == '__main__':
    s = Solution()
    print(s.StrToInt('123'))