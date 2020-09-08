class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("a good   example"))
