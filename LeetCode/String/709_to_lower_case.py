class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        str = list(str)
        for i in range(len(str)):
            if 65 <= ord(str[i]) <= 90:
                str[i] = chr(ord(str[i]) + 32)

        return ''.join(str)


    def toLowerCase_1_line(self, str):
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)


if __name__ == '__main__':
    solution = Solution()
    print(solution.toLowerCase('LOVELY'))


