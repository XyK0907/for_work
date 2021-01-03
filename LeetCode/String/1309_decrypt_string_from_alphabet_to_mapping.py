class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        i = len(s) - 1
        while i > -1:
            if s[i] == '#':
                ch = chr(int(s[i-2:i]) + 96)
                i -= 3
            else:
                ch = chr(int(s[i]) + 96)
                i -= 1
            res.append(ch)
        return ''.join(res)[::-1]

    def freqAlphabets_regex(self, s):
        import re
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))


    def freqAlphabets_cool_solution(self, s):
        for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.freqAlphabets_cool_solution('12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#'))
    print(solution.freqAlphabets_regex('10#11#12'))