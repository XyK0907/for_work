class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        number_list = []
        is_positive = True
        if x >= 0:
            if x < 2**31 -1:

                while x != 0:
                    temp = x % 10
                    print("temp",temp)
                    number_list.append(temp)
                    x = x // 10
                    print("x",x)

                print(number_list)
            else:
                return 0
        else:
            if x > -2**31:
                is_positive = False
                x = -x
                while x != 0:
                    temp = x % 10
                    number_list.append(temp)
                    x = x // 10
                    if x == 0:
                        break
                print(number_list)
            else:
                return 0
        if is_positive:
            reversed_x = 0
            for each in number_list:
                reversed_x = reversed_x * 10 + each
            print(reversed_x)
            if reversed_x < 2**31 -1:
                return reversed_x
            else:
                return 0
        else:
            reversed_x = 0
            for each in number_list:
                reversed_x = reversed_x * 10 + each
            reversed_x = - reversed_x
            print(reversed_x)
            if reversed_x > -2**31:
                return reversed_x
            else:
                return 0


if __name__=="__main__":
    solution = Solution()
    solution.reverse(123)
