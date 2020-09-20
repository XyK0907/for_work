class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        return list(filter(self.same_line, words))

    def same_line(self, word):
        first_row = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'} # set('qwertyuiop')
        second_row ={'a', 's','d', 'f', 'g', 'h', 'j', 'k', 'l'}
        third_row = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        return set(word.lower()) <= first_row or \
               set(word.lower()) <= second_row or \
               set(word.lower())<= third_row

    def findWords1(self, words):
        return [x for x in words if
                set(x).issubset(set("qwertyuiopQWERTYUIOP")) or set(x).issubset(set("asdfghjklASDFGHJKL")) or set(
                    x).issubset(set("zxcvbnmZXCVBNM"))]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))

