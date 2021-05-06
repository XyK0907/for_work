class Solution(object):
    def nextGreaterElements(self, nums): #mei xie chu lai
        """
        time O(n)
        space O(n)
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        length = len(nums)
        res = [-1] * length
        for i in range(length):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(length):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            if not stack:
                break

        return res

    def nextGreaterElements_short(self, nums): #mei xie chu lai
        """
        time O(n)
        space O(n)
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = nums[::-1]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElements([1, 2, 1]))
