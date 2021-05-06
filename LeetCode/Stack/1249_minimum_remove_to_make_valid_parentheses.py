class Solution(object):
    def minRemoveToMakeValid(self, s): #mei xie chu lai
        """
        time O(n)
        space O(n)
        :type s: str
        :rtype: str
        """
        index_to_remove = set()
        stack = []
        for i, char in enumerate(s):
            if char not in '()':
                continue
            if char == '(':
                stack.append(i)
            elif not stack:
                index_to_remove.add(i)
            else:
                stack.pop()
        index_to_remove = index_to_remove.union(set(stack))
        string_builder = []
        for i, char in enumerate(s):
            if i not in index_to_remove:
                string_builder.append(char)
        return ''.join(string_builder)

    def minRemoveToMakeValid_2(self, s): #mei xie chu lai
        """
        首先删除所有有问题的 ")"。
        完成第一步后，留下来的所有字符构成了新的字符串。
        反向扫描字符串，用相同的方法删除无效的 "("。最后反转字符串的顺序即可。
        删除无效的 ")"，然后翻转字符串，再次扫描删除无效的 "("，就得到了最终结果。
        time O(n)
        space O(n)
        :type s: str
        :rtype: str
        """
        def remove_invalid_closing(string, open, close):
            sb = []
            balance = 0
            for ch in string:
                if ch == open:
                    balance += 1
                elif ch == close:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(ch)
            return ''.join(sb)

        s = remove_invalid_closing(s, '(', ')')
        s = remove_invalid_closing(s[::-1], ')', '(')
        return s[::-1]

    def minRemoveToMakeValid_3(self, s): #mei xie chu lai
        """
        这是方法二的简化版本，只需要保持平衡即可，不需要栈，也不需要执行两次完整的字符串扫描。在完成第一步扫描后，查看有多少个需要删除的 "("，
        然后从右侧开始扫描，删除对应个数的 "(" 即可。事实证明，如果删除最右边的 "("，一定可以保证字符串平衡。

        time O(n)
        space O(n)
        :type s: str
        :rtype: str
        """
        # Parse 1: Remove all invalid ")"
        first_parse_chars = []
        balance = 0
        open_seen = 0
        for c in s:
            if c == "(":
                balance += 1
                open_seen += 1
            if c == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_parse_chars.append(c)

        # Parse 2: Remove the rightmost "("
        result = []
        open_to_keep = open_seen - balance
        for c in first_parse_chars:
            if c == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(c)

        return "".join(result)