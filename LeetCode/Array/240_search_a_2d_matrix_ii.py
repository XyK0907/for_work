class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        the same as 74 search a 2d matrix
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        colomns = len(matrix[0])
        row = 0
        colomn = colomns - 1
        while row < rows and colomn >= 0:
            if target == matrix[row][colomn]:
                return True
            elif target > matrix[row][colomn]:
                row += 1
            else:
                colomn -= 1
        return False
