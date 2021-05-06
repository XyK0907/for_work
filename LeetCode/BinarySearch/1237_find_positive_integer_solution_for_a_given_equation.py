"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""

class Solution(object):
    def findSolution(self, customfunction, z):
        """
        In binary search, time complexity is O(XlogY) or O(YlogX)
        In this solution, time complexity is stable O(X + Y).
        Bianry search is really an unnecessay operation, and it won't help improve the conplexity at all.
        Space is O(X)
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        y = 1000
        for x in range(1, 1001):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                res.append([x, y])
        return res
