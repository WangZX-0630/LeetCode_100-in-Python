from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        tmp = [[]]
        tmp2 = []
        candidates.sort()
        for i in range(len(candidates)):
            for c in tmp:
                if candidates[i] + sum(c) > target:
                    continue
                for j in range(int(target / candidates[i]) + 1):
                    if candidates[i] * j + sum(c) < target:
                        tmp2.append(c + [candidates[i]] * j)
                    elif candidates[i] * j + sum(c) == target:
                        combinations.append(c + [candidates[i]] * j)
            tmp = tmp2
            tmp2 = []
        return combinations


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 5], 8))

