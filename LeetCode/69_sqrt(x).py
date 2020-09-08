class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.recursive(x, 0, x)

    def recursive(self, number, start, end):
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if mid ** 2 > number:
            return self.recursive(number,start,mid-1)
        if mid ** 2 < number:
            if (mid + 1) ** 2 > number:
                return mid
            return self.recursive(number,mid+1,end)
        return mid

if __name__ == "__main__":
    solution = Solution()
    # print(solution.example(0.04))
    print(solution.mySqrt(15))