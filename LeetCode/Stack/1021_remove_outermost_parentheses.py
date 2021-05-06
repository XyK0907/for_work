class Solution(object):
    def removeOuterParentheses(self, S):
        """
        time O(n)
        space O(n)
        :type S: str
        :rtype: str
        """
        balance = 0
        string_buffer = []
        for ch in S:
            if ch == '(':
                if balance == 0:
                    balance += 1
                    continue
                else:
                    balance += 1
                    string_buffer.append(ch)
            else:
                balance -= 1
                if balance == 0:
                    continue
                else:
                    string_buffer.append(ch)
        return ''.join(string_buffer)

    def removeOuterParentheses_clear(self, S):
        """
        :type S: str
        :rtype: str
        """
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return ''.join(res)

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeOuterParentheses("(()())(())"))
    print(solution.removeOuterParentheses("(()())(())(()(()))"))
    print(solution.removeOuterParentheses("()()"))
