class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = 0
        cur_length = 0
        max_length = 0
        stuck_index = []
        for i, c in enumerate(s):
            if c == '(':
                stack += 1
                if cur_length != 0:
                    stuck_index.append(i)
            else:   # c == ')'
                if stack > 0:
                    stack -= 1
                    if cur_length != 0:
                        if len(stuck_index) != 0:
                            stuck_index.pop(-1)
                    cur_length += 2
                else:
                    if cur_length > max_length:
                        max_length = cur_length
                    cur_length = 0
        if cur_length > max_length:
            max_length = cur_length

        if len(stuck_index) != 0:
            result_list = []
            result_list.append(self.longestValidParentheses(s[0:stuck_index[0]]))
            result_list.append(self.longestValidParentheses(s[stuck_index[-1]:]))
            for i in range(len(stuck_index) - 1):
                result_list.append(self.longestValidParentheses(s[stuck_index[i]: stuck_index[i + 1]]))
            max_length = max(result_list)

        return max_length


if __name__ == '__main__':
    s = '()(()'
    solution = Solution()
    print(solution.longestValidParentheses(s))
