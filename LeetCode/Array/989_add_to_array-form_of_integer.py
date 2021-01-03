class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        numA = int(''.join(map(str, A)))
        return list(str(numA + K))

    def addToArrayForm_solution(self, A, K):
        """
        Schoolbook Addition
        """
        for i in range(len(A) - 1, -1, -1):
            K, A[i] = divmod(A[i] + K, 10)
        return [int(i) for i in str(K)] + A if K else A


if __name__ == '__main__':
    solution = Solution()
    print(solution.addToArrayForm([1, 2, 0, 0], 34))
    print(solution.addToArrayForm_solution([2, 7, 4], 181))