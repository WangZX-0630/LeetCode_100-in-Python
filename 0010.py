# 对于被.*分割后的子串 子串所匹配对象串的长度由*的数量决定：l = (子串l - n(*), 无穷)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '*' not in p:
            if '.' not in p:
                if s == p:
                    return True
            else:
                if len(s) != len(p):
                    return False
                else:
                    for i, c in enumerate(p):
                        if c == '.':
                            p[i] = s[i]
                    if s == p:
                        return True
            return False
        else:
            l = ''
            repeat_start_index = 0
            for i, c in enumerate(p):
                if c == '*':
                    if p[i - 1] != '.':
                        for j in range(len(l), len(s)):
                            if s[j] == p[i - 1]:
                                l += p[i - 1]
                            else:
                                break
                elif c == '.':
                    l += s[i]
                else:
                    l += p[i]
            print(l)
            if l == s:
                return True
            else:
                return False




a = 'd*.dd*a*'
b = 'ddddaaaa'
solution = Solution()
print(solution.isMatch(b, a))
