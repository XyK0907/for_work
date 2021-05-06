"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

提示：

    所有元素乘积之和不会溢出 32 位整数
    a.length <= 100000

    思路：
        B[0] = A[1] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[0]）
        B[1 ]= A[0] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[1]）
        B[2] = A[0] * A[1] * A[3] * A[4] *....*A[n-1] ;（没有A[2]）

"""

class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        b= [1] * len(a)
        tmp = 1
        for i in range(1,len(a)):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] = b[i] * tmp
        return b