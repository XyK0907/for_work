class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = 0
        right = len(chars) - 1
        repeat = 0
        while left < right:
            if chars[left] == chars[left + 1]:
                chars.pop(left + 1)
                right -= 1
                repeat += 1
            else:
                if repeat == 0:
                    left += 1
                else:
                    for c in str(repeat + 1):
                        chars.insert(left + 1, c)
                        right += 1
                        left += 1
                    left += 1
                    repeat = 0
        if repeat != 0:
            chars.extend(list(str(repeat + 1)))
        print(chars)
        return len(chars)



if __name__ == '__main__':
    solution = Solution()
    print(solution.compress(["a","a","b","b","c","c","c", "d"]))
    print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
