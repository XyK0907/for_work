"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：

    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100

注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        方法一：模拟

        可以模拟螺旋矩阵的路径。初始位置是矩阵的左上角，初始方向是向右，当路径超出界限或者进入之前访问过的位置时，则顺时针旋转，进入下一个方向。

        判断路径是否进入之前访问过的位置需要使用一个与输入矩阵大小相同的辅助矩阵 visited\textit{visited}visited，其中的每个元素表示该位置
        是否被访问过。当一个元素被访问时，将 visited\textit{visited}visited 中的对应位置的元素设为已访问。

        如何判断路径是否结束？由于矩阵中的每个元素都被访问一次，因此路径的长度即为矩阵中的元素数量，当路径的长度达到矩阵中的元素数量时即为完整路
        径，将该路径返回。

        time O(mn)
        space O(mn)

        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix[0] == []:
            return []
        rows = len(matrix)
        colomns = len(matrix[0])
        total = rows * colomns
        visitied = [[False] * colomns for _ in range(rows)]
        ans = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direc_idx = 0
        row, colomn = 0, 0
        for i in range(total):
            ans[i] = matrix[row][colomn]
            visitied[row][colomn] = True
            nxt_row = row + directions[direc_idx][0]
            nxt_colomn = colomn + directions[direc_idx][1]
            if not(0 <= nxt_row < rows and 0 <= nxt_colomn < colomns and visitied[nxt_row][nxt_colomn] == False):
                direc_idx = (direc_idx + 1) % 4
            row += directions[direc_idx][0]
            colomn += directions[direc_idx][1]
        return ans


    def spiralOrder_1(self, matrix):
        """
        可以将矩阵看成若干层，首先输出最外层的元素，其次输出次外层的元素，直到输出最内层的元素。

        定义矩阵的第 kkk 层是到最近边界距离为 kkk 的所有顶点。例如，下图矩阵最外层元素都是第 1 层，次外层元素都是第 2 层，剩下的元素都是第 3 层。

        [[1, 1, 1, 1, 1, 1, 1],
         [1, 2, 2, 2, 2, 2, 1],
         [1, 2, 3, 3, 3, 2, 1],
         [1, 2, 2, 2, 2, 2, 1],
         [1, 1, 1, 1, 1, 1, 1]]
         对于每层，从左上方开始以顺时针的顺序遍历所有元素。假设当前层的左上角位于 (top,left)(\textit{top}, \textit{left})(top,left)，
         右下角位于 (bottom,right)(\textit{bottom}, \textit{right})(bottom,right)，按照如下顺序遍历当前层的元素。

        从左到右遍历上侧元素，依次为 (top,left)(\textit{top}, \textit{left})(top,left) 到 (top,right)(\textit{top},
        \textit{right})(top,right)。

        从上到下遍历右侧元素，依次为 (top+1,right)(\textit{top} + 1, \textit{right})(top+1,right) 到 (bottom,right)(\textit{bottom},
        \textit{right})(bottom,right)。

        如果 left<right\textit{left} < \textit{right}left<right 且 top<bottom\textit{top} < \textit{bottom}top<bottom，
        则从右到左遍历下侧元素，依次为 (bottom,right−1)(\textit{bottom}, \textit{right} - 1)(bottom,right−1) 到
        (bottom,left+1)(\textit{bottom}, \textit{left} + 1)(bottom,left+1)，以及从下到上遍历左侧元素，依次为
         (bottom,left)(\textit{bottom}, \textit{left})(bottom,left) 到 (top+1,left)(\textit{top} + 1, \textit{left})(top+1,left)。

        遍历完当前层的元素之后，将 left\textit{left}left 和 top\textit{top}top 分别增加 111，将 right\textit{right}right 和
        bottom\textit{bottom}bottom 分别减少 111，进入下一层继续遍历，直到遍历完所有元素为止。

        time O(mn)
        space O(10

        :param matrix:
        :return:
        """
        if matrix == [] or matrix[0] == []:
            return []
        rows = len(matrix)
        colomns = len(matrix[0])
        ans = []
        left, top = 0, 0
        right, bottom = colomns - 1, rows - 1
        while left <= right and top <= bottom:
            for colomn in range(left, right + 1):
                ans.append(matrix[top][colomn])
            for row in range(top + 1, bottom + 1):
                ans.append(matrix[row][right])
            if left < right and top < bottom:
                for colomn in range(right - 1, left, -1):
                    ans.append(matrix[bottom][colomn])
                for row in range(bottom, top, -1):
                    ans.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom -1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder_1([[6,9,7]]))




