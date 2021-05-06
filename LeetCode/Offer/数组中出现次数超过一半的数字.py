"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
示例1
输入
[1,2,3,2,2,2,5,4,2]

返回值
2
"""

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        time O（n）
        space O(n)
        :param numbers:
        :return:
        """
        dic = {}
        for number in numbers:
            dic[number] = dic.get(number, 0) + 1
        for number, frequency in dic.items():
            if frequency > len(numbers) // 2:
                return number
        return 0

    def MoreThanHalfNum_Solution_best(self, numbers):
        """
        time O(n)
        space O(1)
        :param numbers:
        :return:
        """
        # 这个操作就是建立在出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，所以如果存在这个数，最后count
        # 肯定不为0的
        count = 1
        number = numbers[0]
        for i in numbers[1:]:
            if number == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    number = i
                    count += 1

        sum = 0
        for j in numbers:
            if j == number:
                sum += 1

        return number if sum > len(numbers) // 2 else 0

if __name__ == '__main__':
    s = Solution()
    print(s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))