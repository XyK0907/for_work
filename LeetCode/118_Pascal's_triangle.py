class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list_out = []
        list_previous = []
        for i in range(1,numRows+1):
            new_list_in = [1]
            if i ==2:
                new_list_in = [1,1]
            if i > 2:
                for j in range(2, i):
                    element = list_previous[j-2] + list_previous[j-1]
                    new_list_in.append(element)
                new_list_in.append(1)
            list_out.append(new_list_in)
            list_previous = new_list_in
        return list_out

if __name__ == "__main__":
    solution = Solution()
    # print(solution.example(0.04))
    print(solution.generate(6))