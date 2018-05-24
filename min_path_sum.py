# https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not list(filter(None, grid)):
            return 0
        T = [[float('inf') for _ in row] for row in grid]
        T[0][0] = grid[0][0]
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if (i + j) == 0:
                    continue
                T[i][j] = min([T[i - 1][j] + col, T[i][j - 1] + col])
        return T[-1][-1]
