class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        row = [i for i in range(len(mat))]
        row_sum = [sum(each) for each in mat]
        return list(zip(*sorted([(a, b) for a, b in zip(row, row_sum)], key=lambda x: x[1])[:k]))[0]


    def kWeakestRows_solution(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        return sorted(range(len(mat)), key=lambda x:sum(mat[x]))[:k]



if __name__ == "__main__":
    solution = Solution()
    print(solution.kWeakestRows_solution([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))
    print(solution.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2))