class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = []
        for i in range(0,len(s), 2 * k):
            cut = s[i:i + k]
            s_list.append(cut[::-1])
            s_list.append(s[i + k:i + 2 * k])

        return ''.join(s_list)

    def reverseStr_other_solution(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])

        return ''.join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseStr('abcdefghijklmnopqrstuvw', 3))