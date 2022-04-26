class Solution:
    def isValid(self, s: str) -> bool:
        Left_dict = {
            '(': 1,
            '[': 2,
            '{': 3
        }
        Right_dict = {
            ')': -1,
            ']': -2,
            '}': -3
        }
        cur_list = []
        for c in s:
            if c in Left_dict.keys():
                cur_list.append(Left_dict[c])
            if c in Right_dict.keys():
                if len(cur_list) == 0 or cur_list[-1] + Right_dict[c] != 0:
                    return False
                cur_list.pop()
        if len(cur_list) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('((([{}]))[()])'))

