from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        paths = []
        begin_point = []
        board_characters = set()
        for i in range(m):
            for j in range(n):
                board_characters.add(board[i][j])
                if board[i][j] == word[0]:
                    begin_point.append((i, j))
        for w in word:
            if w not in board_characters:
                return False

        if len(begin_point) != 0 and len(word) > 1:
            for i in range(len(begin_point)):
                paths.append([begin_point[i]])

                if self.back_track(paths[0], board, paths[0][0], 1, word) is True:
                    return True
                else:
                    paths = []
        elif len(begin_point) != 0 and len(word) <= 1:
            return True
        return False


    def back_track(self, path, board, cur_index, target_index, word):
        target = word[target_index]
        candidates = []
        if cur_index[0] != 0:
            if board[cur_index[0] - 1][cur_index[1]] == target and (cur_index[0] - 1, cur_index[1]) not in path:
                candidates.append((cur_index[0] - 1, cur_index[1]))
        if cur_index[0] != len(board) - 1:
            if board[cur_index[0] + 1][cur_index[1]] == target and (cur_index[0] + 1, cur_index[1]) not in path:
                candidates.append((cur_index[0] + 1, cur_index[1]))
        if cur_index[1] != 0:
            if board[cur_index[0]][cur_index[1] - 1] == target and (cur_index[0], cur_index[1] - 1) not in path:
                candidates.append((cur_index[0], cur_index[1] - 1))
        if cur_index[1] != len(board[0]) - 1:
            if board[cur_index[0]][cur_index[1] + 1] == target and (cur_index[0], cur_index[1] + 1) not in path:
                candidates.append((cur_index[0], cur_index[1] + 1))
        if len(candidates) != 0:
            if target_index == len(word) - 1:
                return True
            else:
                for i in range(len(candidates)):
                    if self.back_track(path + [candidates[i]], board, candidates[i], target_index + 1, word) is True:
                        return True
        else:
            return False




if __name__ == '__main__':
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(solution.exist(board, word))

