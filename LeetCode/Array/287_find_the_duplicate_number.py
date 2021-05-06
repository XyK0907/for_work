class Solution(object):
    def findDuplicate(self, nums): #mei xie chu lai
        """
        same idea as in Linked List Cycle II
        time O(n)
        space O(1)
        :type nums: List[int]
        :rtype: int
        """
        # Find the intersection point of the two runners.
        hare = tortoise = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        #Find the "entrance" to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return hare
