from pythonds.basic import Stack

class Solution(object):
    def isValid_stack(self, s):  #导入栈模块
        """
        :type s: str
        :rtype: bool
        """
        opens = '([{'
        closes = ')]}'
        parstack = Stack()
        balance = True

        for each in s:
            if each in '([{':
                parstack.push(each)
            else:
                if parstack.isEmpty():
                    balance = False
                else:
                    top = parstack.pop()
                    if opens.index(top) != closes.index(each):
                        balance = False
        if balance and parstack.isEmpty():
            return True
        else:
            return False

    def isValid(self, s):  #没有栈模块
        """
        :type s: str
        :rtype: bool
        """
        # opens = '([{'
        # closes = ')]}'
        pairs = {'(':')', '[':']', '{':'}'}
        parstack = []

        for each in s:
            if each in '([{':
                parstack.append(each)
            else:
                if len(parstack) == 0:
                    return False
                else:
                    # if opens.index(top) != closes.index(each):
                    if pairs[parstack.pop()] != each:
                        return False
        return len(parstack) == 0

    def isValid_similar(self, s):
        """
        time O(n)
        space O(n)
        :param s:
        :return:
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []



if __name__=="__main__":
    solution = Solution()
    print(solution.isValid("{[]}"))