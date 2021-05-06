"""
Facebook interviewers like this question and propose it in four main variations. The choice of algorithm should be based
on the input format:

    Strings (the current problem). Use schoolbook digit-by-digit addition. Note, that to fit into constant space is not
    possible for languages with immutable strings, for example, for Java and Python. Here are two examples:

        Add Binary: sum two binary strings.

        Add Strings: sum two non-negative numbers in a string representation without converting them to integers directly.

    Integers. Usually, the interviewer would ask you to implement a sum without using + and - operators.
    Use bit manipulation approach. Here is an example:
        Sum of Two Integers: Sum two integers without using + and - operators.

    Arrays. The same textbook addition. Here is an example:
        Add to Array Form of Integer.

    Linked Lists. Sentinel Head + Textbook Addition. Here are some examples:

        Plus One.

        Add Two Numbers.

        Add Two Numbers II.

"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        Time O(max(n1,n2))
        Space O(max(n1, n2))
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 > -1 or p2 > -1 or carry:
            x1 = ord(num1[p1]) - ord('0') if p1 > -1 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 > -1 else 0
            carry = x1 + x2 + carry
            value = carry % 10
            carry = carry // 10
            res.append(value)
            p1 -= 1
            p2 -= 1

        return ''.join(str(x) for x in res[::-1])