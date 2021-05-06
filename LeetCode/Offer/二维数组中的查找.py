"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和
一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。

给定 target = 20，返回 false。

限制：
0 <= n <= 1000
0 <= m <= 1000
注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
"""

class Solution(object):
    def findNumberIn2DArray(self, matrix, target): #mei zuo chu lai
        """
        Or start from left bottom
        从二维数组的右上角开始查找。如果当前元素等于目标值，则返回 true。
        如果当前元素大于目标值，则移到左边一列。如果当前元素小于目标值，则移到下边一行。
        可以证明这种方法不会错过目标值。如果当前元素大于目标值，说明当前元素的下边的所有元素都一定大于目标值，
        因此往下查找不可能找到目标值，往左查找可能找到目标值。如果当前元素小于目标值，说明当前元素的左边的所有元素都一定小于目标值，
        因此往左查找不可能找到目标值，往下查找可能找到目标值。
        time O(m + n)
        space O(1)
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        rows = len(matrix)
        colomns = len(matrix[0])
        row = 0
        colomn = colomns - 1
        while row < rows and colomn >=0:
            if matrix[row][colomn] == target:
                return True
            elif matrix[row][colomn] > target:
                colomn -= 1
            else:
                row += 1
        return False

"""
一种是：
把每一行看成有序递增的数组，
利用二分查找，
通过遍历每一行得到答案，
时间复杂度是nlogn
"""
