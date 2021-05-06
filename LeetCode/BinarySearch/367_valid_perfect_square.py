class Solution(object):
    def isPerfectSquare(self, num):
        """
        binary search
        :type num: int
        :rtype: bool
        """
        l, r = 1, num
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def isPerfectSquare_newton(self, num):
        """
        use Newton's method
        :type num: int
        :rtype: bool
        """
        r = num
        while r * r > num:
            r = (r + num/r) // 2
            return r * r == num

    def isPerfectSquare_mathtrick(self, num):
        """
        Math Trick for Square number is 1+3+5+ ... +(2n-1)
        :type num: int
        :rtype: bool
        """
        i = 1
        while(num > 0):
            num -= i
            i += 2
        return num == 0

    def isPerfectSquare_naive(self, num):
        """
        linear method(naive)
        :type num: int
        :rtype: bool
        """
        i = 1
        while i ** 2 <= num:
            if i ** 2 == num:
                return True
            else:
                i += 1
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPerfectSquare(225))