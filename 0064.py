from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return sum(grid[0])
        else:
            m = len(grid)
            n = len(grid[0])
            dp = [[255 for i in range(n)] for j in range(m)]
            dp[-1][0] = 0
            dp[0][-1] = 0

            for i in range(m):
                for j in range(n):
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

            return dp[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(solution.minPathSum(grid))
