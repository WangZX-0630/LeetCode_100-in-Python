from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        elif n == 1:
            return ['()']
        else:
            tmp = []
            results = []
            for i in range(1, n + 1):
                listl = self.generateParenthesis(i - 1)
                listr = self.generateParenthesis(n - i)
                for p in listl:
                    for q in listr:
                        tmp.append(str('(' + p + ')' + q))

            for result in tmp:
                if len(result) != 2*n:
                    results.append(str(result + ')' * (2*n - len(result))))
                else:
                    results.append(result)
            results = list(set(results))
            return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(4))

# (()())()
