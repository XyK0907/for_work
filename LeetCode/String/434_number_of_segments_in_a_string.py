class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())


    def countSegments1(self, s):
        return sum(s[i] != ' ' and (i == 0 or s[i - 1] == ' ') for i in range(len(s)))

if __name__ == '__main__':
    solution = Solution()
    print(solution.countSegments('Hello, my name is John'))