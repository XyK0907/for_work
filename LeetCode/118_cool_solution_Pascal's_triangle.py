class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]


if __name__ == "__main__":
    solution = Solution()
    # print(solution.example(0.04))
    print(solution.generate(6))