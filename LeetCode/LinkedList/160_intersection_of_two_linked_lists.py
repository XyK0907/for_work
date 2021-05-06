# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic = set()
        while headA and headB:
            if headA not in dic and headB not in dic:
                dic.add(headA)
                if headB not in dic:
                    dic.add(headB)
                else:
                    return headB
                headA = headA.next
                headB = headB.next
            elif headA in dic:
                return headA
            else:
                return headB
        while headA:
            if headA not in dic:
                dic.add(headA)
                headA = headA.next
            else:
                return headA
        while headB:
            if headB not in dic:
                dic.add(headB)
                headB = headB.next
            else:
                return headB
        return None

    def getIntersectionNode_2_pointers(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None

    # the idea is if you switch head, the possible difference between length would be countered.
    # On the second traversal, they either hit or miss.
    # if they meet, pa or pb would be the node we are looking for,
    # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None

    def getIntersectionNode_1(self, headA, headB):
        """
        Time O(n)
        Space O(1)
        :param headA:
        :param headB:
        :return:
        """
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA
    

    """
    Brute Force
    For each node ai in list A, traverse the entire list B and check if any node in list B coincides with ai.
    Time complexity : O(mn).
    
    Space complexity : O(1).
    """

    """
    Hash Table
    Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: 
    if bi appears in the hash set, then bi is the intersection node.
    Time complexity : O(m+n).
    
    Space complexity : O(m) or O(n).
    """
