class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        Say we have our answer as a stack with rightmost asteroid top, and a new asteroid comes in.
        If new is moving right (new > 0), or if top is moving left (top < 0), no collision occurs.

        Otherwise, if abs(new) < abs(top), then the new asteroid will blow up; if abs(new) == abs(top) then both
        asteroids will blow up; and if abs(new) > abs(top), then the top asteroid will blow up (and possibly more
        asteroids will, so we should continue checking.)

        time O(n)
        space O(n)
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for each in asteroids:
            while stack and each < 0 < stack[-1]:
                if abs(each) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(each) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(each)
        return stack


