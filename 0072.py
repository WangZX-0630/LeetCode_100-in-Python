class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        else:
            dp = [[0 for j in range(len(word2))] for i in range(len(word1))]
            for j in range(len(word2)):
                if word1[0] in word2[0: j + 1]:
                    dp[0][j] = j
                else:
                    dp[0][j] = j + 1
            for i in range(len(word1)):
                if word2[0] in word1[0: i + 1]:
                    dp[i][0] = i
                else:
                    dp[i][0] = i + 1

            for i in range(1, len(word1)):
                for j in range(1, len(word2)):
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

            return dp[len(word1) - 1][len(word2) - 1]


if __name__ == '__main__':
    solution = Solution()
    word1 = 'horse'
    word2 = 'ros'
    print(solution.minDistance(word1, word2))

                
