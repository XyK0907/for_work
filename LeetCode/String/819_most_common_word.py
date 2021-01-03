import re
from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’| '
        words_list = [word.lower() for word in re.split(pattern, paragraph) if word != '']
        dic = Counter(words_list)
        for item in dic.most_common():
            if item[0] not in banned:
                return item[0]

    def mostCommonWord_cool_solution(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())  # \w 匹配字母或数字或下划线或汉字, + 重复一次或更多次
        return Counter(w for w in words if w not in ban).most_common(1)[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.mostCommonWord_cool_solution("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
