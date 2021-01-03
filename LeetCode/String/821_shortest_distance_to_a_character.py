class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = []
        for i in range(len(S)):
            if S[i] == C:
                pos.append(i)
        j = 0
        res = []
        for k in range(len(S)):
            minimum = 0
            if k < pos[j]:
                if j == 0:
                    minimum = pos[j] - k
                else:
                    minimum = min(pos[j] - k, k - pos[j-1])
            elif k > pos[j]:
                j += 1
                if j == len(pos):
                    minimum = k - pos[j - 1]
                    j -= 1
                else:
                    minimum = min(pos[j] - k, k - pos[j-1])
            res.append(minimum)

        return res

    def shortestToChar_cool_solution(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n, pos = len(S), -float('inf')
        res = [n] * n
        for i in list(range(n)) + list(range(n)[::-1]):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res

    def shortestToChar_cool_solution1(self, S, C):  ## two pointer
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res = [0 if c == C else n for c in S]
        for i in range(1, n):
            res[i] = min(res[i], res[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            res[i] = min(res[i], res[i + 1] + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestToChar_cool_solution1('aaba', 'b'))
    # print(solution.shortestToChar('loveleetcode', 'e'))

