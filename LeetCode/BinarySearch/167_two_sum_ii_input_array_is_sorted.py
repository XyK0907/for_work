class Solution(object):
    def twoSum(self, numbers, target): #mei xie chu lai
        """
        two Pointer
        O(n) time and O(1) space
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1

    def twoSum_dictionary(self, numbers, target): #mei xie chu lai
        """
        Dictionary
        O(n) time and O(n) space
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num] + 1, i + 1]
            dic[num] = i

    def twoSum_binarysearch(self, numbers, target): #mei xie chu lai
        """
        binary search
        O(nlogn) time and O(1) space
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l<=r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
if __name__=="__main__":
    solution = Solution()
    print(solution.twoSum_dictionary([0, 0, 3, 4], 0))
    print(solution.twoSum_binarysearch([2, 3, 4, 5], 8))
    print(solution.twoSum([-1, 0], -1))