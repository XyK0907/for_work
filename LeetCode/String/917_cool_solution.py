import re


class Solution:
    def reverseOnlyLetters(self, S):
        r = [s for s in S if s.isalpha()]
        return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))

    def reverseOnlyLetters_regex(self, S):
        return re.sub(r'[A-Za-z]', "{}", S).format(*[c for c in S[::-1] if c.isalpha()])