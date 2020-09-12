import re
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} #使用set更快
        # vowels = set(list('aeiouAEIOU'))
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


    def reverseVowels_regex(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)  # (?i)表示忽略大小写
        # repl参数每次返回一个值，用来替换s匹配pattern的字符。
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseVowels('leetcode'))