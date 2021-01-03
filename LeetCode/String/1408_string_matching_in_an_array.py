class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        words = sorted(words, key=len)
        def recursive(words):
            longest = words.pop()
            for each in words:
                if each in longest:
                    res.append(each)
            if words == []:
                return res
            else:
                return recursive(words)
        return list(set(recursive(words)))

    def stringMatching_cool_solution(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        arr = ' '.join(words)
        subStr = [i for i in words if arr.count(i) >= 2]

        return subStr

    def stringMatching_brute(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        ans = []
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.stringMatching_cool_solution(['mass', 'as', 'hero', 'superhero']))
    print(solution.stringMatching_cool_solution(['leetcode', 'et', 'code']))
    print(solution.stringMatching_cool_solution(['blue', 'green', 'bu']))
    print(solution.stringMatching_cool_solution(["leetcoder","leetcode","od","hamlet","am"]))