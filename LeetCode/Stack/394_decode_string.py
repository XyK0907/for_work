class Solution(object):
    def decodeString(self, s): #mei xie chu lai
        """
        Stack
        time O(S+|s|)
        space O(S)
        本题难点在于括号内嵌套括号，需要从内向外生成与拼接字符串，这与栈的先入后出特性对应。

        算法流程：

            构建辅助栈 stack， 遍历字符串 s 中每个字符 c；
                当 c 为数字时，将数字字符转化为数字 multi，用于后续倍数计算；
                当 c 为字母时，在 res 尾部添加 c；
                当 c 为 [ 时，将当前 multi 和 res 入栈，并分别置空置 000：
                    记录此 [ 前的临时结果 res 至栈，用于发现对应 ] 后的拼接操作；
                    记录此 [ 前的倍数 multi 至栈，用于发现对应 ] 后，获取 multi × [...] 字符串。
                    进入到新 [ 后，res 和 multi 重新记录。
                当 c 为 ] 时，stack 出栈，拼接字符串 res = last_res + cur_multi * res，其中:
                    last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a；
                    cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2。
            返回字符串 res。
        :type s: str
        :rtype
        """
        stack = []
        curstring = ''
        curnum = 0
        for c in s:
            if c == '[':
                stack.append(curstring)
                stack.append(curnum)
                curnum = 0
                curstring = ''
            elif c == ']':
                num = stack.pop()
                prevstring = stack.pop()
                curstring = prevstring + num * curstring
            elif c.isdigit():
                curnum = curnum * 10 + int(c)
            else:
                curstring = curstring + c
        return curstring

    def decodeString_recursive(self, s): #mei xie chu lai
        """
        Recursion
        time O(n)
        space O(n)

        总体思路与辅助栈法一致，不同点在于将 [ 和 ] 分别作为递归的开启与终止条件：
        当 s[i] == ']' 时，返回当前括号内记录的 res 字符串与 ] 的索引 i （更新上层递归指针位置）；
        当 s[i] == '[' 时，开启新一层递归，记录此 [...] 内字符串 tmp 和递归后的最新索引 i，并执行 res + multi * tmp 拼接字符串。
        遍历完毕后返回 res。

        :param s:
        :return:
        """
        def dfs(s, i):
            res, multi = '', 0
            while i < len(s):
                if s[i].isdigit():
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i+1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s, 0)



if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))


