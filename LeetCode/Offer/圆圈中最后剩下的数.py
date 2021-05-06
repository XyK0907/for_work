'''
题目：每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了
一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,
继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额
有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
'''

class Solution(object):
    def lastRemaining(self, n, m):
        """
        classic Josephus problem
        解法一：用循环链表实现
        解法二：数组实现
        解法三：用数学公式求解
        f(n,m) = (f(n−1,m) + m) % n
        若已知N-1个人时，胜利者的下标位置位 f ( N − 1 , M )，则N个人的时候，就是往后移动M为，
        (因为有可能数组越界，超过的部分会被接到头上，所以还要模N)，既 f ( N , M ) = ( f ( N − 1 , M ) + M ) % n
        time O(n)
        space O(n)
        :type n: int
        :type m: int
        :rtype: int
        """
        sys.setrecursionlimit(100000)
        def f(n, m):
            if n == 0:
                return n
            x = f(n -1, m)
            return (x + m) % n
        return f(n, m)


    def lastRemaining_iter(self, n, m):
        """
        time O(n)
        space O(1)
        :type n: int
        :type m: int
        :rtype: int
        """
        f = 0
        for i in range(2, n + 1):
            f = (f + m) % i
        return f

if __name__ == '__main__':
    solution = Solution()
    print(solution.lastRemaining(10, 17))
    print(solution.lastRemaining(5, 3))