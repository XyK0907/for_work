class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        result = 0
        for i in range(0,len(s)-1):
            if dictionary[s[i]]< dictionary[s[i+1]]:
                result -= dictionary[s[i]]
            else:
                result += dictionary[s[i]]
        return result + dictionary[s[-1]]



if __name__=="__main__":
    solution = Solution()
    solution.romanToInt("MCMXCIV")