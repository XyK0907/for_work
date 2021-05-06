class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # if rowIndex == 0:
        #     return [1]
        # if rowIndex == 1:
        #     return [1,1]
        # if rowIndex > 1:
        #     list_previous = [1,1]
        #     for i in range(3, rowIndex+2):
        #         new_list_in = [1]
        #         for j in range(2,i):
        #             element = list_previous[j-2] + list_previous[j-1]
        #             new_list_in.append(element)
        #         new_list_in.append(1)
        #         list_previous = new_list_in
        #     return list_previous
        def recursive(outputlist):
            new_list = [1]
            for i in range(1, len(outputlist)):
                new_list.append(outputlist[i -1] + outputlist[i])
            new_list.append(1)
            return new_list

        out = [1]
        for j in range(0, rowIndex):
            out = recursive(out)
        return out

    def getRow_cool(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row

    def getRow_1(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                pascal[j] += pascal[j - 1]
        return pascal

if __name__ == "__main__":
    solution = Solution()
    # print(solution.example(0.04))
    print(solution.getRow(3))