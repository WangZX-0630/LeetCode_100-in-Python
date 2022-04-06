class Solution(object):
    def findMedianGivenLength(self, nums, length):
        if length % 2 == 0:
            return float((nums[int(length / 2 - 1)] + nums[int(length / 2)]) / 2.0)
        else:
            return float(nums[int(length / 2)])

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            return self.findMedianGivenLength(nums2, len(nums2))
        elif len(nums2) == 0:
            return self.findMedianGivenLength(nums1, len(nums1))
        else:
            if nums1[-1] < nums2[0]:
                if len(nums1) > len(nums2):
                    return self.findMedianGivenLength(nums1, len(nums1) + len(nums2))
                elif len(nums1) < len(nums2):
                    return self.findMedianGivenLength(nums2, len(nums2) - len(nums1))
                else:
                    return float((nums1[-1] + nums2[0]) / 2.0)
            elif nums1[0] > nums2[-1]:
                if len(nums1) > len(nums2):
                    return self.findMedianGivenLength(nums1, len(nums1) - len(nums2))
                elif len(nums1) < len(nums2):
                    return self.findMedianGivenLength(nums2, len(nums1) + len(nums2))
                else:
                    return float((nums1[-1] + nums2[0]) / 2.0)
            else:
                nums1_offset = 0
                nums2_offset = 0
                k = int((len(nums1) + len(nums2)) / 2)
                while k > 1:
                    index_1 = nums1_offset + int(k / 2) - 1
                    index_2 = nums2_offset + int(k / 2) - 1
                    if index_1 > len(nums1) - 1:
                        index_1 = len(nums1) - 1
                        if nums1[index_1] <= nums2[index_2]:
                            return self.findMedianGivenLength(nums2, len(nums2) - len(nums1))
                        else:
                            nums2_offset += int(k / 2)
                            k = k - int(k / 2)
                    elif index_2 > len(nums2) - 1:
                        index_2 = len(nums2) - 1
                        if nums1[index_1] >= nums2[index_2]:
                            return self.findMedianGivenLength(nums1, len(nums1) - len(nums2))
                        else:
                            nums1_offset += int(k / 2)
                            k = k - int(k / 2)
                    else:
                        if nums1[index_1] <= nums2[index_2]:
                            nums1_offset += int(k / 2)
                        elif nums1[index_1] > nums2[index_2]:
                            nums2_offset += int(k / 2)
                        k = k - int(k / 2)
                if len(nums1) >= nums1_offset + 1 and len(nums2) >= nums2_offset + 1:
                    if min(nums1[nums1_offset], nums2[nums2_offset]) == nums1[nums1_offset]:
                        if len(nums1) >= nums1_offset + 2 and nums1[nums1_offset + 1] < nums2[nums2_offset]:
                            num1 = nums1[nums1_offset]
                            num2 = nums1[nums1_offset + 1]
                        else:
                            num1 = nums1[nums1_offset]
                            num2 = nums2[nums2_offset]
                    elif min(nums1[nums1_offset], nums2[nums2_offset]) == nums2[nums2_offset]:
                        if len(nums2) >= nums2_offset + 2 and nums1[nums1_offset] > nums2[nums2_offset + 1]:
                            num1 = nums2[nums2_offset]
                            num2 = nums2[nums2_offset + 1]
                        else:
                            num1 = nums1[nums1_offset]
                            num2 = nums2[nums2_offset]
                    if (len(nums1) + len(nums2)) % 2 == 0:
                        return float((num1 + num2) / 2)
                    else:
                        return float(max(num1, num2))
                elif len(nums1) < nums1_offset + 1:
                    return self.findMedianGivenLength(nums2, len(nums2) - len(nums1))
                else:
                    return self.findMedianGivenLength(nums1, len(nums1) - len(nums2))


import math
solution = Solution()
nums_list1 = [1]
nums_list2 = [2, 3]
print(solution.findMedianSortedArrays(nums_list1, nums_list2))



