from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_zero_index = -1
        for i in range(len(nums)):
            if nums[i] == 0 and i != len(nums) - 1:
                counter = 0
                for j in range(last_zero_index + 1, i):
                    if nums[j] + j <= i:
                        counter += 1
                if counter == i - last_zero_index - 1:
                    return False

        return True



if __name__ == '__main__':
    solution = Solution()
    nums = [10, 0]
    print(solution.canJump(nums))
