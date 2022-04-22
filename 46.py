from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 or len(nums) == 0:
            return [nums]
        combinations = []
        for i in range(len(nums)):
            for c in self.permute(list(nums[0:i] + nums[i+1:len(nums)])):
                combinations.append([nums[i]] + c)

        return combinations


if __name__ == '__main__':
    solution = Solution()
    print(len(solution.permute([0, 1])))

