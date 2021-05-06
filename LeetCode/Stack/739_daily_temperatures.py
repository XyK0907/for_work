class Solution(object):
    def dailyTemperatures(self, T):
        """
        Time O(n)
        Space O(W) W is the number of allowed values for T[i]
        :type T: List[int]
        :rtype: List[int]
        """
        length = len(T)
        res = [0] * length
        stack = []
        for i in range(length):
            while stack and T[stack[-1]] < T[i]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res

    def dailyTemperatures_another(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        length = len(T)
        res = [0] * length
        stack = []
        for i in range(length - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures_another(T = [73, 74, 75, 71, 69, 72, 76, 73]))