"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        """
        time O(target)
        space O(1)
        :param tsum:
        :return:
        """
        l, r = 1, 2
        ans = []
        while l < r:
            sum = (l + r) * (r - l + 1) / 2
            if sum == tsum:
                ans.append([x for x in range(l, r + 1, 1)])
                l = l + 1
            elif sum < tsum:
                r += 1
            else:
                l += 1
        return ans

    def FindContinuousSequence_root(self, tsum):
        res = []
        # y不能超过target的中值,即y<=target//2 + 1,range函数左开右闭,所以这里是+2
        for y in range(1, tsum // 2 + 2):
            # 应用我们的求根公式
            x = (1/4 + y**2 + y - 2 * tsum) ** (1/2) + 0.5
            # 我们要确保x不能是复数，且x必须是整数
            if type(x) != complex and x - int(x) == 0:
                res.append(list(range(int(x), y + 1)))
        return res



if __name__ == '__main__':
    solution = Solution()
    print(solution.FindContinuousSequence(15))