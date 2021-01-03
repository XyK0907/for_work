class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        for each in J:
            ans += S.count(each)
        return ans

    def numJewelsInStones1(self, J, S):
        return sum(map(J.count, S))

    def numJewelsInStones2(self, J, S):
        return sum(map(S.count, J))

    def numJewelsInStones3(self, J, S):
        return sum(s in set(J) for s in S)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numJewelsInStones1('aA', 'aAAbbbbbb'))
