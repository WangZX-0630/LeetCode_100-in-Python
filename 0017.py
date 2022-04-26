from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        buffer = []
        result = []
        for digit in digits:
            letters = num_dict[digit]
            for c in letters:
                if len(buffer) == 0:
                    result += c
                else:
                    for string in buffer:
                        result.append(str(string + c))
            buffer = result
            result = []
        return buffer

solution = Solution()
print(solution.letterCombinations('234'))
