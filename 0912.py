import random
from typing import List
import time


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.qSort(nums, 0, len(nums) - 1)
        return nums

    def median3(self, nums: List[int], left: int, right: int) -> int:
        center = int((left + right) / 2)
        if nums[left] > nums[center]:
            nums[left], nums[center] = nums[center], nums[left]
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[center] > nums[right]:
            nums[center], nums[right] = nums[right], nums[center]
        nums[center], nums[right - 1] = nums[right - 1], nums[center]
        return nums[right - 1]

    def qSort(self, nums: List[int], left: int, right: int):
        cut_off = 10
        if (right - left) > cut_off:
            pivot = self.median3(nums, left, right)
            i = left
            j = right - 1
            while 1:
                i += 1
                j -= 1
                while nums[i] < pivot: i += 1
                while nums[j] > pivot: j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    break
            nums[i], nums[right - 1] = nums[right - 1], nums[i]
            self.qSort(nums, left, i - 1)
            self.qSort(nums, i + 1, right)
        else:
            self.insertionSort(nums, left, right)

    def insertionSort(self, nums: List[int], left: int, right: int):
        for i in range(left, right + 1):
            num = nums[i]
            j = i
            while j > left and num < nums[j - 1]:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = num


if __name__ == '__main__':
    l = []
    solution = Solution()
    random.seed(1234)
    for i in range(100):
        l.append(random.randint(0, 100))
    print(l)
    st = time.perf_counter()
    solution.sortArray(l)
    et = time.perf_counter()
    print(l)
    print('cost time: %f s' % (et - st))



