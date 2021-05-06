
class Solution:
    def findLongestWord(self, s, dictionary) :
        dictionary = sorted(dictionary, key=lambda x: (-len(x), x))
        print(dictionary)
        for word in dictionary:
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            if i == len(word):
                return word
        return ""

    def findLongestWord_without_sorting(self, s, dictionary):
        """
        Since sorting the dictionary could lead to a huge amount of extra effort, we can skip the sorting and directly
        look for the strings xxx in the unsorted dictionary ddd such that xxx is a subsequence in sss. If such a string
        xxx is found, we compare it with the other matching strings found till now based on the required length and
        lexicographic criteria. Thus, after considering every string in ddd, we can obtain the required result.
        :param s:
        :param dictionary:
        :return:
        """
        maxstr = ''
        for word in dictionary:
            if self.issubsequence(word, s):
                if len(word) > len(maxstr) or (len(word) == len(maxstr) and word < maxstr):
                    maxstr = word
        return maxstr

    def issubsequence(self, word, s):
        i = j = 0
        while j < len(word):
            if i == len(s):
                break
            if word[j] == s[i]:
                j += 1
            i += 1
        return j == len(word)
if __name__ == '__main__':
    solution = Solution()
    print(solution.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))