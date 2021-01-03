class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(B) == len(A) and B in A + A

if __name__ == '__main__':
    solution = Solution()
    print(solution.rotateString('abcde', 'abced'))
