"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "

限制：
0 <= s 的长度 <= 50000
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        dic = Counter(s)
        if 1 in dic.values():
            for each in s:
                if dic[each] == 1:
                    return each
        else:
            return ""

        # res=list(filter(lambda c:self.s.count(c)==1,self.s))
        # return res[0] if res else "#"

"""
在哈希表的基础上，有序哈希表中的键值对是 按照插入顺序排序 的。基于此，可通过遍历有序哈希表，实现搜索首个 “数量为 1 的字符”。
Python 3.6 后，默认字典就是有序的，因此无需使用 OrderedDict()
"""