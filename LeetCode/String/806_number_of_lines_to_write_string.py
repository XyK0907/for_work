class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        sum_per_line = 0
        lines_nr = 1
        for letter in S:
            sum_per_line = sum_per_line + widths[ord(letter) - 97]
            if sum_per_line > 100:
                sum_per_line = widths[ord(letter) - 97]
                lines_nr += 1
        return lines_nr, sum_per_line




if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfLines([4,20,20,20,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))
