class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ## 更好的方法是把n转成str
        n_appear = [n]
        while n != 1:
            temp = 0
            while n:
                n, r = divmod(n, 10)
                temp += r * r
            if temp in n_appear:
                return False
            else:
                n_appear.append(temp)
                n = temp
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19))