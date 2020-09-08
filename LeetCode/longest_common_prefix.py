class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for j in range(0,len(strs[0])):
            letter = strs[0][j]
            index = 0
            for i in range(1,len(strs)):
                if strs[i][j] == letter:
                    index += 1
            if index == len(strs)-1:
                print(letter)


if __name__=="__main__":
    solution = Solution()
    strs = ["flower","flow","flight"]
    solution.longestCommonPrefix(strs)
