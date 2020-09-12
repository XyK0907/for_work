class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtyp
        """
        dic = {}
        for i, ch in enumerate(s):
            if t[i] not in dic.values():
                if ch not in dic.keys():
                    dic[ch] = dic.get(ch, t[i])
                else:
                    return False
            else:
                if ch not in dic.keys() or dic.get(ch) != t[i]:
                    return False

        return True



if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic('aa', 'ab'))