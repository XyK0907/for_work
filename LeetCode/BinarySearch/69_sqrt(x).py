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

    def mySqrt_bineary_search(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        l, r = 2, x // 2
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r

if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt_bineary_search(6))