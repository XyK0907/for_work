class Solution(object):
    def plusOne(self,digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]

    def plusOne_1(self,digits):
        # s1 = "-"
        # s2 = ""
        # seq = ("r", "u", "n", "o", "o", "b")  # 字符串序列
        # print(s1.join(seq))
        # print(s2.join(seq))

        # >> > map(square, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方
        # [1, 4, 9, 16, 25]

        return map(int, list(str(int(''.join(map(str, digits))) + 1)))











if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
    solution.plusOne_1([1,2,3])