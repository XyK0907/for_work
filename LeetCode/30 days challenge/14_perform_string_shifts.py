class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        left = 0
        right = 0
        for each in shift:
            if each[0] == 0:
                left += each[1]
            else:
                right += each[1]
        print(left)
        print(right)
        count = (left-right) % len(s)
        print(count)
        if left < right:
            s = s[count:] + s[0: count]
        else:
            s = s[count:] + s[0:count]
        return s

if __name__ == '__main__':
    solution = Solution()
    print(solution.stringShift("xqgwkiqpif",[[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]))