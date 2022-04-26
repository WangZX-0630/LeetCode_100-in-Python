from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(int(n / 2)):
            cur_length = n - 1 - i * 2
            tmp_list = matrix[i][i: i + cur_length]
            for j in range(cur_length):
                matrix[i][i + j] = matrix[n - 1 - j - i][i]
                matrix[n - 1 - j - i][i] = matrix[n - 1 - i][n - 1 - j - i]
                matrix[n - 1 - i][n - 1 - j - i] = matrix[i + j][n - 1 - i]
                matrix[i + j][n - 1 - i] = tmp_list[j]


if __name__ == '__main__':
    solution = Solution()
    n = 10
    matrix = []
    for i in range(n):
        matrix.append([i * n + j for j in range(n)])
    solution.rotate(matrix)
    print(matrix)
