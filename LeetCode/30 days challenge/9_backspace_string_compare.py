class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = '#'
        S = self.backspace(s,S)
        T = self.backspace(s,T)
        if S == T:
            return True
        else:
            return False

    def backspace(self, s, S):
        while s in S:
            index = S.find(s)
            if index == 0:
                S = S[index+1:]
            else:
                S = S[:index-1] + S[index+1:]
        return S


if __name__ == '__main__':
    solution = Solution()
    solution.backspaceCompare("a#c","b")