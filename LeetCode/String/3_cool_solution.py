class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length

    def lengthOfLongestSubstring_1(self, string):
        """
        Time:  O(n)
        Space: O(k)
        [k = length of the longest substring w/o repeating characters]
        """
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(string) and right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(string[left])
                left += 1
        return longest


if __name__ == '__main__':
    solution = Solution()
    # print(solution.lengthOfLongestSubstring('au'))
    # print(solution.lengthOfLongestSubstring_1('pwwkew'))
    # print(solution.lengthOfLongestSubstring('bbbbbb'))
    print(solution.lengthOfLongestSubstring_1('abcabcbb'))