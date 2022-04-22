from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        sort_index = sorted(range(len(height)), key=lambda k: height[k])
        i = 1
        n = len(height)
        cover_l = min(sort_index[n - i], sort_index[n - i - 1])
        cover_r = max(sort_index[n - i], sort_index[n - i - 1])
        total_water = self.cal_volume(height[cover_l:cover_r + 1])
        i += 2
        while cover_r - cover_l < len(height) and i <= n:
            if sort_index[n - i] < cover_l:
                total_water += self.cal_volume(height[sort_index[n - i]:cover_l + 1])
                cover_l = sort_index[n - i]
            elif sort_index[n - i] > cover_r:
                total_water += self.cal_volume(height[cover_r:sort_index[n - i] + 1])
                cover_r = sort_index[n - i]
            i += 1
        return total_water

    def cal_volume(self, height: List[int]) -> int:
        water_height = min(height[0], height[-1])
        volume = 0
        for i in range(len(height)):
            if height[i] < water_height:
                volume += water_height - height[i]
        return volume

if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
