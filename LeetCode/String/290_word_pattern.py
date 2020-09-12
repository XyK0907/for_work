class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        if len(str_list) != len(pattern):
            return False
        return len(set(zip(pattern, str_list))) == len(set(pattern)) == len(set(str_list))

    def wordPattern1(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        for i, ch in enumerate(pattern):
            dic1[ch] = dic1.get(ch, []) + [i]
        for i, word in enumerate(str.split()):
            dic2[word] = dic2.get(word, []) + [i]

        return sorted(dic1.values()) == sorted(dic2.values())

    def wordPattern2(self, pattern, str):
        """
        faster than 100%
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return map(pattern.find, pattern) == map(str.split().index, str.split())

if __name__ == '__main__':
    solution = Solution()
    solution.wordPattern('aba', 'cat cat cat dog')