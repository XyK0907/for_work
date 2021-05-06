"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:

输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""


class Solution:
    def Permutation(self, ss):
        ss = sorted(list(ss), key=ord)
        ans = []
        ls = []
        for i in range(len(ss)):





if __name__ == '__main__':
    s = Solution()
    print(s.Permutation("cab"))