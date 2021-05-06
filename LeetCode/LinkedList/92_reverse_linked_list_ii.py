# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        my solution
        time O(N)
        space O(1)
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        m_ = m
        if m == n:
            return head
        prev = None
        pm, pn, head_last = head, head, head
        while m - 1 or n:
            if m - 1:
                pm = pm.next
                if m - 2:
                    head_last = head_last.next
                m -= 1
            if n :
                pn = pn.next
                n -= 1
        p = pm
        while pm != pn:
            curr = pm
            pm = pm.next
            curr.next = prev
            prev = curr
        if m_ != 1:
            head_last.next = prev
        else:
            head = prev
        p.next = pm
        return head

    def reverseBetween_recursion(self, head, m, n):
        """
        Back Tracking, hard to understanding
        Time O(N)
        Soace O(N)
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head

    def reverseBetween_iterative(self, head, m, n):
        """
        idea same as mine, but more concise
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1
        con, tail = prev, cur
        while n:
            third = cur
            cur = cur.next
            third.next = prev
            prev = third
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head



