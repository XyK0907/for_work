class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = list('aeiouAEIOU')
        s_list = S.split()
        for i in range(len(s_list)):
            if s_list[i][0] in vowel:
                s_list[i] += 'ma' + 'a' * (i+1)
            else:
                s_list[i] = s_list[i][1:] + s_list[i][0] + 'ma' + 'a' * (i+1)
        return ' '.join(s_list)

    def toGoatLatin_one_line(self, S):
        """
        :type S: str
        :rtype: str
        """
        return ' '.join(
            (w if w[0].lower() in 'aeiou' else w[1:] + w[0]) + 'ma' + 'a' * (i + 1) for i, w in enumerate(S.split()))



if __name__ == '__main__':
    solution = Solution()
    print(solution.toGoatLatin_one_line("Each word consists of lowercase and uppercase letters only"))
