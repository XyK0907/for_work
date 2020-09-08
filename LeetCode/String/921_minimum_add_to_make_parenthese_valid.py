class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        balance = 0
        close_first = 0
        for each in S:
            if each == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    close_first += 1
        return balance + close_first


if __name__ == '__main__':
    solution = Solution()
    print(solution.minAddToMakeValid('()))(('))
