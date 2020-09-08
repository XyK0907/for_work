class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] in '(*':
                left += 1
            else:
                left -= 1
            if s[len(s)-i-1] in '*)':
                right += 1
            else:
                right -= 1
            if left < 0 or right < 0:
                return False
        return True


    def checkValidString_1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_max = 0
        close_min = 0

        for c in s:
            if c == "(":
                close_max += 1
                close_min += 1
            elif c == ")":
                close_max -= 1
                close_min -= 1
            else:
                close_max += 1
                close_min -= 1

            if close_max < 0:
                return False
            if close_min < 0:
                close_min = 0

        return close_min == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkValidString_1('(*)()'))