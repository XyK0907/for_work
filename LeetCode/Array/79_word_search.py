class Solution(object):
    def exist(self, board, word):  #mei xie chu lai
        """
        这是一个使用回溯算法解决的问题，涉及的知识点有 DFS 和状态重置

        设函数 check(i,j,k)判断以网格的 (i,j)位置出发，能否搜索到单词 word[k..]，
        其中 word[k..] 表示字符串 word 从第 k 个字符开始的后缀子串。如果能搜索到，则返回 true，反之返回 false。
        函数 check(i,j,k) 的执行步骤如下：

        如果 board[i][j]≠s[k]，当前字符不匹配，直接返回 false。
        如果当前已经访问到字符串的末尾，且对应字符依然匹配，此时直接返回 true。
        否则，遍历当前位置的所有相邻位置。如果从某个相邻位置出发，能够搜索到子串 word[k+1..]，则返回 true，否则返回 false。
        这样，我们对每一个位置 (i,j) 都调用函数 check(i,j,0)进行检查：只要有一处返回 true，就说明网格中能够找到相应的单词，否则说明不能找到。

        为了防止重复遍历相同的位置，需要额外维护一个与 board 等大的 visited 数组，用于标识每个位置是否被访问过。
        每次遍历相邻位置时，需要跳过已经被访问的位置。

        Time: 一个非常宽松的上界为 O(MN⋅3^L)，其中 M,N为网格的长度与宽度，L为字符串 word 的长度。
        在每次调用函数 check 时，除了第一次可以进入 4 个分支以外，其余时间我们最多会进入 3 个分支（因为每个位置只能使用一次，所以走过来的分支没法走回去）。
        由于单词长为 L，故 check(i, j, 0)) 的时间复杂度为 O(3^L)，而我们要执行 O(MN) 次检查。
        然而，由于剪枝的存在，我们在遇到不匹配或已访问的字符时会提前退出，终止递归流程。因此，实际的时间复杂度会远远小于 Θ(MN⋅3^L)
        Space: O(MN)。我们额外开辟了 O(MN)的 visited 数组，同时栈的深度最大为 O(min(L,MN))

        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < h and 0 <= new_j < w:
                    if (new_i, new_j) not in visited:
                        if check(new_i, new_j, k + 1):
                            return True

            visited.remove((i, j))
            return False

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))



