class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for i in arr:
            if i + 1 in arr:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countElements([1,1,2,2]))


