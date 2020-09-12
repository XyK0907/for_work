class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type S: str
        :rtype: str
        """
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if ord(s[left].lower()) < 97 or ord(s[left]) > 122:
                left = left + 1
            elif ord(s[right].lower()) < 97 or ord(s[right]) > 122:
                right = right - 1
            else:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left, right = left + 1, right - 1
        return ''.join(s)

    def reverseOnlyLetters1(self, s):
        """
        :type S: str
        :rtype: str
        """
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalpha():
                left = left + 1
            elif not s[right].isalpha():
                right = right - 1
            else:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        return ''.join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseOnlyLetters1('a-bC-dEf-ghIj'))


