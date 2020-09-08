class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex > 1:
            list_previous = [1,1]
            for i in range(3, rowIndex+2):
                new_list_in = [1]
                for j in range(2,i):
                    element = list_previous[j-2] + list_previous[j-1]
                    new_list_in.append(element)
                new_list_in.append(1)
                list_previous = new_list_in
            return list_previous


if __name__ == "__main__":
    solution = Solution()
    # print(solution.example(0.04))
    print(solution.getRow(2))