from typing import List


class Solution:
    def insertion_sort(self, intervals):
        for i in range(1, len(intervals)):
            tmp = intervals[i]
            for j in range(i - 1, -1, -1):
                if intervals[j][0] > tmp[0]:
                    intervals[j + 1] = intervals[j]
                elif intervals[j][0] == tmp[0]:
                    if intervals[j][1] > tmp[1]:
                        intervals[j + 1] = intervals[j]
                else:
                    j = j + 1
                    break
            intervals[j] = tmp

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.insertion_sort(intervals)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                tmp = result.pop()
                result.append([tmp[0], max(intervals[i][1], tmp[1])])
            else:
                result.append(intervals[i])
        return result


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 2], [2, 4], [8, 19], [15, 18]]
    print(solution.merge(intervals))

