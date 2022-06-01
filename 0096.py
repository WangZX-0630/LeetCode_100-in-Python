class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n)]
        dp[0] = 1
        for i in range(1, n):
            dp[i] = 2 * dp[i - 1]
            for j in range(0, i - 1):
                dp[i] += dp[i - 2 - j] * dp[j]
        return dp[n - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(1))

