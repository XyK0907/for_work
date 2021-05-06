class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') < 2 and 'LLL' not in s

    def checkRecord_re(self, s):
        """
        . : 匹配任何除了换行以外的单个字符。

        * : 匹配 0 个或者 大于 0 个 * 符号前面的表达式。

        .* : 匹配任何字符串

        a|b : 要么匹配 a 要么匹配 b
        :type s: str
        :rtype: bool
        """
        import re
        return not re.search('A.*A|LLL', s)



if __name__ == '__main__':
    solution = Solution()
    print(solution.checkRecord('LALL'))