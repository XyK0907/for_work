class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]

        return ' '.join(s_list)

    def reverseWords_short(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join(x[::-1] for x in s.split())

    def reverseWords_special(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join(s.split()[::-1])[::-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords_special("Let's take LeetCode contest"))