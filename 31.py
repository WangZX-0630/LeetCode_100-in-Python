from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 0 and len(nums) != 1:
            cur_index = len(nums) - 2
            resort_list = []
            resort_list.append(nums[-1])
            while nums[cur_index] >= nums[cur_index + 1] and cur_index >= 0:
                resort_list.append(nums[cur_index])
                cur_index -= 1
            if cur_index == -1:
                nums.sort()
            else:
                cur_num = nums[cur_index]
                resort_list.sort()
                for num in resort_list:
                    if num > nums[cur_index]:
                        nums[cur_index] = num
                        resort_list.remove(num)
                        break
                resort_list.append(cur_num)
                resort_list.sort()
                for num in resort_list:
                    cur_index += 1
                    nums[cur_index] = num


if __name__ == '__main__':
    list1 = [4, 3, 2, 1]
    solution = Solution()
    solution.nextPermutation(list1)
    print(list1)


