from typing import List


#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         three_sum_list = []
#         two_num_sum = [[0] * len(nums) for _ in range(len(nums) - 1)]
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 two_num_sum[i][j] = nums[i] + nums[j]
#         for i in range(len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 for k in range(j + 1, len(nums)):
#                     if two_num_sum[j][k] + nums[i] == 0:
#                         list = [nums[i], nums[j], nums[k]]
#                         list.sort()
#                         if list not in three_sum_list:
#                             three_sum_list += [list]
#         return three_sum_list

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         three_sum_list = []
#         index_mid = int(len(nums) / 2)
#         max_num_index = index_mid + 1
#         min_num_index = index_mid - 1
#         for i in range(index_mid, 0, -1):
#             if nums[i] + nums[i - 1] + nums[-1] < 0:
#                 break
#             for j in range(i - 1, -1, -1):
#                 for k in range(max_num_index, len(nums)):
#                     if nums[k] + nums[i] + nums[j] > 0:
#                         max_num_index = k
#                         break
#                     elif nums[i] + nums[j] + nums[k] == 0:
#                         max_num_index = k
#                         if [nums[j], nums[i], nums[k]] not in three_sum_list:
#                             three_sum_list += [[nums[j], nums[i], nums[k]]]
#             max_num_index = i
#
#         for i in range(index_mid, len(nums) - 1):
#             if nums[i] + nums[i + 1] + nums[0] > 0:
#                 break
#             for j in range(i + 1, len(nums)):
#                 for k in range(min_num_index, -1, -1):
#                     if nums[k] + nums[i] + nums[j] < 0:
#                         min_num_index = k
#                         break
#                     elif nums[k] + nums[i] + nums[j] == 0:
#                         min_num_index = k
#                         if [nums[k], nums[i], nums[j]] not in three_sum_list:
#                             three_sum_list += [[nums[k], nums[i], nums[j]]]
#             min_num_index = i
#
#         return three_sum_list

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        three_sum_list = []
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] > 0:
                break
            three = n - 1
            target = -nums[first]
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while three > second and nums[three] + nums[second] > target:
                    three -= 1
                if second == three:
                    break
                if nums[second] + nums[three] == target:
                    three_sum_list.append([nums[first], nums[second], nums[three]])
        return three_sum_list

solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
