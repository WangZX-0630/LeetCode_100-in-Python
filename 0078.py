from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = [[]]
        for i in range(len(nums)):
            n = len(sub_sets)
            for j in range(n):
                sub_sets.append(sub_sets[j] + [nums[i]])
        return sub_sets


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1]))


