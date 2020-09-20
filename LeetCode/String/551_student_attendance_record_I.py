class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') < 2 and 'LLL' not in s



if __name__ == '__main__':
    solution = Solution()
    print(solution.checkRecord('LALL'))