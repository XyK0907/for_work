class Solution(object):
    def reverseString(self, s):
        """
        Do not allocate extra space for another array, you must do this by modifying the input array
        in-place with O(1) extra memory.
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseString_1(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        s.reverse()
        # return s[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseString(["h","e","l","l","o"]))

