import itertools
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def backspace(S):
            stack_s = []
            for each in S:
                if each == '#':
                    if stack_s != []:
                        stack_s.pop()
                else:
                    stack_s.append(each)
            return ''.join(stack_s)
        return backspace(S) == backspace(T)


    def backspaceCompare_cool_solution(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare_cool_solution("##ac#", "bd#c#"))
