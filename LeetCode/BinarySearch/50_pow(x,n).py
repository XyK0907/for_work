class Solution(object):
    def myPow(self, x, n): #mei xie chu lai
        """
        本题的方法被称为「快速幂算法」，有递归和迭代两个版本。
        方法一：快速幂 + 递归

        「快速幂算法」的本质是分治算法。举个例子，如果我们要计算 x64x^{64}x64，我们可以按照：
        x→x2→x4→x8→x16→x32→x64x \to x^2 \to x^4 \to x^8 \to x^{16} \to x^{32} \to x^{64} x→x2→x4→x8→x16→x32→x64
        的顺序，从 x 开始，每次直接把上一次的结果进行平方，计算 6 次就可以得到 x64 的值，而不需要对 x 乘 63 次 xx。
        再举一个例子，如果我们要计算 x77x^{77}x77，我们可以按照：
        x→x2→x4→x9→x19→x38→x77x \to x^2 \to x^4 \to x^9 \to x^{19} \to x^{38} \to x^{77} x→x2→x4→x9→x19→x38→x77
        的顺序，在 x→x2x \to x^2x→x2，x2→x4x^2 \to x^4x2→x4，x19→x38x^{19} \to x^{38}x19→x38 这些步骤中，我们直接把上一次的
        结果进行平方，而在 x4→x9x^4 \to x^9x4→x9，x9→x19x^9 \to x^{19}x9→x19，x38→x77x^{38} \to x^{77}x38→x77 这些步骤中，
        我们把上一次的结果进行平方后，还要额外乘一个 xxx。

        但如果我们从右往左看，分治的思想就十分明显了：

        当我们要计算 xnx^nxn 时，我们可以先递归地计算出 y=x⌊n/2⌋y = x^{\lfloor n/2 \rfloor}y=x⌊n/2⌋，其中 ⌊a⌋\lfloor a \rfloor⌊a⌋
        表示对 aaa 进行下取整；
        根据递归计算的结果，如果 nnn 为偶数，那么 xn=y2x^n = y^2xn=y2；如果 nnn 为奇数，那么 xn=y2∗xx^n = y^2 * xxn=y2∗x；
        递归的边界为 n=0n = 0n=0，任意数的 000 次方均为 111。

        time O(logn)
        space O(logn)

        :type x: float
        :type n: int
        :rtype: float
        """
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        return quickMul(n) if n >=0 else 1.0 / quickMul(-n)


    def myPow_iter(self, x, n): #bu hui
        """
        快速幂 + 迭代
        time O(logn)
        space O(1)

        :type x: float
        :type n: int
        :rtype: float
        """

        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


