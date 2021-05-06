class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


    def isAnagram1(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2


    def is_anagram(self,s, t):
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2


if __name__=="__main__":
    solution = Solution()
    print(solution.isAnagram('anagram','nagaram'))
    print(solution.isAnagram('rat','cat'))