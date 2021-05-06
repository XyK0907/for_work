"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        left, right = 0, len(array) - 1
        while left < right:
            if array[left] % 2 == 1:
                left += 1
                continue
            if array[right] % 2 == 0:
                right -= 1
                continue
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        return array

    def reOrderArray_extraspace(self, array):
        odd = []
        even = []
        for each in array:
            if each % 2 == 0:
                even.append(each)
            else:
                odd.append(each)
        return odd + even

if __name__ == '__main__':
    s = Solution()
    print(s.reOrderArray_extraspace([1,2,3,4,5,6,7,8,9]))