class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters) - 1
        larger = letters[-1]
        while l <= r:
            mid = l + (r - l) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                larger = letters[mid]
                r = mid - 1
        if r == len(letters) - 1:
            return letters[0]
        else:
            return larger

    def nextGreatestLetter_record_letters_seen(self, letters, target):
        """
        Time: O(n)
        Spece: O(1)
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand

    def nextGreatestLetter_linear_scan(self, letters, target):
        """
        Time: O(n)
        Spece: O(1)
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for c in letters:
            if c > target:
                return c
        return letters[0]

    def nextGreatestLetter_bisect(self, letters, target):
        """
        Time: O(log n)
        Spece: O(1)
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        import bisect
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreatestLetter_record_letters_seen(["c", "f", "j"], 'a'))
    print(solution.nextGreatestLetter_bisect(["c", "f", "j"], 'c'))
    print(solution.nextGreatestLetter(["c", "f", "j"], 'd'))
    print(solution.nextGreatestLetter(["c", "f", "j"], 'g'))
    print(solution.nextGreatestLetter(["c", "f", "j"], 'j'))
    print(solution.nextGreatestLetter(["c", "f", "j"], 'k'))