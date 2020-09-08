class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            print([0]+row)
            print(row+[0])
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

if __name__ == "__main__":
    solution = Solution()
    print(solution.getRow(3))