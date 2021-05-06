class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def recursive(outputlist):
            ll = outputlist[-1]
            new_list = [1]
            for i in range(1, len(ll)):
                new_list.append(ll[i -1] + ll[i])
            new_list.append(1)
            outputlist.append(new_list)
            return outputlist

        if not numRows:
            return []

        out = [[1]]
        for j in range(1, numRows):
            out = recursive(out)
        return out

    def generate_cool(self, numRows):
        """
        explanation: Any row can be constructed using the offset sum of the previous row
            1 3 3 1 0
         +  0 1 3 3 1
         =  1 4 6 4 1
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]

    def generate_dp(self, numRows):
        """
        time O(n^2)
        space O(n^2)
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

if __name__ == "__main__":
    solution = Solution()
    # print(solution.example(0.04))
    print(solution.generate(1))