import re
import itertools

class Solution(object):
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
            # 「(.)\1」匹配两个连续的相同字符
            # re.sub(r'\s', lambda m: '[' + m.group(0) + ']', text, 0)；将字符串中的空格' '替换为'[ ]'
            #group（0）就是匹配正则表达式整体结果, group(1) 列出第一个括号匹配部分
        return s

    def countAndSay1(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s

    def countAndSay2(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s

    def countAndSay_3(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n - 1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index - 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index - 1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s


if __name__=="__main__":
    solution = Solution()
    print(solution.countAndSay2(4))