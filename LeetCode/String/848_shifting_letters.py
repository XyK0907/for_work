class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        time O(n)
        space O(n)
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        sumall = sum(shifts)
        S = list(S)
        for i in range(len(S)):
            if i != 0:
                sumall = sumall - shifts[i - 1]
            n = ord(S[i]) + sumall%26
            if n <= ord('z'):
                S[i] = chr(n)
            else:
                S[i] = chr(n - ord('z') + ord('a') - 1)

        return ''.join(S)


if __name__ == '__main__':
    solution = Solution()
    print(solution.shiftingLetters('abc', [3, 5, 9]))
    print(solution.shiftingLetters('ruu', [26, 9, 17]))
