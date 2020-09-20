class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

    def judgeCircle1(self, moves):
        from collections import Counter
        c = Counter(moves)
        return c['U'] == c['D'] and c['L'] == c['R']


if __name__ == '__main__':
    solution = Solution()
    print(solution.judgeCircle('LDRRLRUULR'))