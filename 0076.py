class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dp = [100001 for i in range(len(s))]
        table = {}
        index = {}
        l = []
        for j in range(len(t)):
            if t[j] not in table.keys():
                table[t[j]] = 1
                index[t[j]] = [-1]
                l.append(t[j])
            else:
                table[t[j]] += 1
                index[t[j]].append(-1)
        flag = -1
        dic = table.copy()
        for i in range(len(s)):
            if s[i] not in t:
                dp[i] = dp[i - 1]
            else:
                if flag == -1:
                    if dic[s[i]] > 0:
                        dic[s[i]] -= 1
                        j = 0
                        while index[s[i]][j] != -1 and j < len(index[s[i]]):
                            j += 1
                        index[s[i]][j] = i
                    else:
                        index[s[i]].pop(0)
                        index[s[i]].append(i)
                    if sum(dic.values()) == 0:
                        flag = 0
                        min_index = 100001
                        for j in range(len(index)):
                            if index[l[j]][0] < min_index:
                                min_index = index[l[j]][0]
                        dp[i] = i - min_index + 1
                elif flag == 0:
                    index[s[i]].pop(0)
                    index[s[i]].append(i)
                    min_index = 100001
                    for j in range(len(index)):
                        if index[l[j]][0] < min_index:
                            min_index = index[l[j]][0]
                    dp[i] = i - min_index + 1

        if min(dp) < 100001:
            return s[dp.index(min(dp)) - min(dp) + 1: dp.index(min(dp)) + 1]
        else:
            return ''


if __name__ == '__main__':
    solution = Solution()
    s = 'ADOBECODEBANC'
    t = 'ABC'
    print(solution.minWindow(s, t))
