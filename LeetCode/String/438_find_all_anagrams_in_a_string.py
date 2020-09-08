class Solution(object):
    def findAnagrams(self, s, p):  #超时，未通过
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dict_p = {}
        dict_s = {}
        res = []
        for item in p:
            dict_p[item] = dict_p.get(item, 0) + 1
        for i in range(len(s) - len(p) + 1):
            slice = s[i: len(p) + i]
            for item in slice:
                dict_s [item]= dict_s.get(item, 0) + 1
            if dict_p == dict_s:
                res.append(i)
            dict_s.clear()
        return res


if __name__=="__main__":
    solution = Solution()
    print(solution.findAnagrams('abab', 'ab'))
    print(solution.findAnagrams('cbaebabacd', "abc"))