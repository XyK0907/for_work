class Solution:
    ##二分法，非迭代
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot

        return right

if __name__ == "__main__":
    solution = Solution()
    # print(solution.example(0.04))
    print(solution.mySqrt(15))