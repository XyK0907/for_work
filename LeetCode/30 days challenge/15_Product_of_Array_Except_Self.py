class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [1]
        b = [1]
        n = len(nums)
        for i in range(n-1):
            a.append(a[i] * nums[i])
            b.append(b[i] * nums[n - i - 1])
        for j in range(n):
            a[j] = a[j] * b[n - j - 1]
        return a





if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))