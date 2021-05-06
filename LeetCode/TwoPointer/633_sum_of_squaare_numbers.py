import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        ll = [x for x in range(round(math.sqrt(c)) + 1)]
        l, r = 0, len(ll)
        while l <= r:
            if l * l + r * r == c:
                return True
            elif l * l + r * r < c:
                l += 1
            else:
                r -= 1
        return False

    def judgeSquareSum_hashmap(self, c: int) -> bool:
        seen = set()
        for i in range(round(math.sqrt(c) + 1)):
            seen.add(i * i)
            if c - i * i in seen:
                return True
        return False
