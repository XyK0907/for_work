class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            # if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
            #     return mid
            # elif arr[mid + 1] > arr[mid]:
            #     l = mid + 1
            # elif arr[mid - 1] > arr[mid]:
            #     r = mid - 1
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

    def peakIndexInMountainArray_index(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return arr.index(max(arr))

if __name__ == "__main__":
    solution = Solution()
    print(solution.peakIndexInMountainArray([0,1,0]))
    print(solution.peakIndexInMountainArray([0,2,1,0]))
    print(solution.peakIndexInMountainArray([0,10,5,2]))
    print(solution.peakIndexInMountainArray([3,4,5,1]))
    print(solution.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))