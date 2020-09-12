class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for each in s:
            dic[each] = dic.get(each, 0) + 1
        for i, ch in enumerate(s):
            if dic[ch] == 1:
                return i

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstUniqChar("loveleetcode"))
    print(solution.firstUniqChar("leetcode"))