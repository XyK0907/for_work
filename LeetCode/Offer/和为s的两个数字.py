"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
返回值描述:
对应每个测试案例，输出两个数，小的先输出。

输入
[1,2,4,7,11,15],15

返回值
[4,11]
"""

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        """

        :param array:
        :param tsum:
        :return:
        """
        start, end = 0, len(array) - 1
        ans = []
        while start <= end:
            if array[start] + array[end] == tsum:
                ans.append(array[start])
                ans.append(array[end])
                return ans
            elif array[start] + array[end] < tsum:
                start += 1
            else:
                end -= 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.FindNumbersWithSum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 21))