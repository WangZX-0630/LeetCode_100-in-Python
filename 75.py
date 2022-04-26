from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        total_nums = 0
        i = 0
        while total_nums < n:
            if nums[i] == 0:
                nums.insert(0, 0)
                nums.pop(i + 1)
                i += 1
            elif nums[i] == 2:
                nums.insert(n, 2)
                nums.pop(i)
            else:
                i += 1
            total_nums += 1


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 0, 1]
    solution.sortColors(nums)
    print(nums)

