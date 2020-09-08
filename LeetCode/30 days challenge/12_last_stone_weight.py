class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = sorted(stones)
        while len(stones) > 1:
            stones[-2] = stones[-1] - stones[-2]
            del stones[-1]
            stones = sorted(stones)
            if 0 in stones:
                stones.remove(0)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

    def cool_lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            a = max(stones)
            stones.remove(a)
            b = max(stones)
            stones.remove(b)
            if (a!=b):
                stones.append(a-b)
        return stones[0] if stones else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.cool_lastStoneWeight([2,2]))
