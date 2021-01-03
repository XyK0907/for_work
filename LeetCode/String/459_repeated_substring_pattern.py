class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype
        """
        for i in range(1, len(s)):
            if s[:i] * (len(s) // i) == s:
                return True
        return False

    def repeatedSubstringPattern_cool_solution(self, str):

        """
        Basic idea:

        First char of input string is first char of repeated substring
        Last char of input string is last char of repeated substring
        Let S1 = S + S (where S in input string)
        Remove 1 and last char of S1. Let this be S2
        If S exists in S2 then return true else false
        Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]
        Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is present in a rotation of itself for all values of R such that 0 < R < len(S)
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedSubstringPattern_cool_solution('abab'))
    print(solution.repeatedSubstringPattern('aba'))
    print(solution.repeatedSubstringPattern('abcabcabcabc'))