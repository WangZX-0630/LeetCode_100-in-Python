from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    solution = Solution()
    for i in range(8):
        print(solution.search(nums, i))


