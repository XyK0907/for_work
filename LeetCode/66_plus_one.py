class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #与最优答案思路一样，但是写的一点都不简洁
        total = 0
        new_digits = []
        for i, number in enumerate(digits[::-1]):
            total = total + number * 10** i
        total = total +1
        cishu = len(str(total))
        while cishu:
            result = total//(10**(cishu-1))
            total = total%(10**(cishu-1))
            new_digits.append(result)
            cishu -= 1
        return new_digits





if __name__=="__main__":
    solution = Solution()
    print(solution.plusOne([1,2,3]))
    # solution.plusOne([4,3,2,1])