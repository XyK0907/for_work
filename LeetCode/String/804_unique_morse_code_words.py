class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                      "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # res = {}
        # for word in words:
        #     morse = ''.join(morse_code[ord(_) - 97] for _ in word)
        #     res[morse] = res.get(morse, None)
        res = {''.join(morse_code[ord(_) - 97] for _ in word) for word in words}
        return len(res)



if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

