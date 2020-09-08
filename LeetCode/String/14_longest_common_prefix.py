class Solution(object):
    def longestCommonPrefix_last(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str = ""
        if strs == []:  #如果列表是空
            return str
        for j in range(0,len(strs[0])):  #第一个单词的每一个字母
            letter = strs[0][j]
            index = 0
            for i in range(1,len(strs)):  #之后每一个单词
                word_length = len(strs[i])  #获取每个单词长度
                if j < word_length:
                    if strs[i][j] == letter:  #比较每个字母
                        index += 1
            if index == len(strs)-1:  #每一个单词都有这个字母
                str = str + letter
            else:
                break
        return str

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # shortword = strs[0]
        # shortlength = len(strs[0])
        # for each in strs:
        #     if len(each) < shortlength:
        #         shortlength = len(each)
        #         shortword = each
        shortword = min(strs, key=len)
        for index, letter in enumerate(shortword):
            for other in strs:
                if other[index] != letter:
                    return shortword[:index]
        return shortword






if __name__=="__main__":
    solution = Solution()
    strs = ["flower","flow", 'flight']
    # strs =  ["dog","racecar","car"]
    # strs = ['', '']
    print(solution.longestCommonPrefix(strs))