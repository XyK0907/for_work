class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        substring = [s[0]]
        count_max = 1
        for i in range(1, len(s)):
            if s[i] not in substring:
                substring.append(s[i])
            else:
                count_max = max(count_max, len(substring))
                index = substring.index(s[i])
                substring = substring[index + 1:]
                substring.append(s[i])

        return max(count_max, len(substring))


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('au'))
    print(solution.lengthOfLongestSubstring('pwwkew'))
    print(solution.lengthOfLongestSubstring('bbbbbb'))
    print(solution.lengthOfLongestSubstring('abcabcbb'))