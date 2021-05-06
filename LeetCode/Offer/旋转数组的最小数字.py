"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1

示例 2：

输入：[2,2,2,0,1]
输出：0

"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        l, r = 0, len(rotateArray) - 1
        if rotateArray[r] > rotateArray[0]:
            return rotateArray[0]

        while l <= r:
            mid = l + (r - l) // 2
            if rotateArray[mid] > rotateArray[mid + 1]:
                return rotateArray[mid + 1]
            if rotateArray[mid - 1] > rotateArray[mid]:
                return rotateArray[mid]
            if rotateArray[mid] > rotateArray[0]:
                l = l + 1
            else:
                r = r - 1