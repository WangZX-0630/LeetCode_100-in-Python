from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] >= dp[i - 1] + nums[i]:
                dp.append(nums[i])
            elif dp[i - 1] + nums[i] > nums[i]:
                dp.append(dp[i - 1] + nums[i])
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
