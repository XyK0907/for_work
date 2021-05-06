"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压
入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

输入
[1,2,3,4,5],[4,3,5,1,2]

返回值
false
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        """

        :param pushV:
        :param popV:
        :return:
        """
        stack = []
        i = 0
        while i < len(pushV) and pushV[i] != popV[0]:
            stack.append(pushV[i])
            i += 1
        i += 1

        for j in range(1, len(popV)):
            if popV[j] > popV[j - 1]:
                while pushV[i] != popV[j]:
                    stack.append(pushV[i])
                    i += 1
                i += 1
            else:
                element = stack.pop()
                if element != popV[j]:
                    return False
        if stack == []:
            return True
        else:
            return False

    def IsPopOrder_concise(self, pushV, popV):
        """
        time O(n)
        space O(n)
        :param pushV:
        :param popV:
        :return:
        """
        stack, i = [], 0
        for num in pushV:
            stack.append(num)
            while stack and stack[-1] == popV[i]:
                stack.pop()
                i += 1
        return not stack

if __name__ == '__main__':
    solution = Solution()
    print(solution.IsPopOrder([1,2,3,4,5], [4,5,3,2,1]))
    print(solution.IsPopOrder([1,2,3,4,5], [4,3,5,2,1]))
    print(solution.IsPopOrder([1,2,3,4,5], [4,3,5,1,2]))
    print(solution.IsPopOrder([1], [2]))

