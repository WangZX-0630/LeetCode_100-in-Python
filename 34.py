from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        elif nums[0] == nums[-1]:
            if nums[0] == target:
                return [0, len(nums) - 1]
            else:
                return [-1, -1]
        else:
            left = 0
            right = len(nums) - 1

            index = -1
            while left <= right:
                mid = int((left + right) / 2)
                if target == nums[mid]:
                    index = mid
                    break
                elif target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
            if index == -1:
                return [-1, -1]
            i = index
            j = index
            while nums[i - 1] == target or nums[(j + 1) % len(nums)] == target:
                if nums[i - 1] == target:
                    i = i - 1
                if nums[(j + 1) % len(nums)] == target:
                    j = j + 1

            return [i, j]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2, 3, 3, 3, 4]
    for i in range(5):
        print(solution.searchRange(nums, i))

