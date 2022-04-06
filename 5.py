# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2:
#             return s
#         elif len(s) == 2:
#             if s[0] == s[1]:
#                 return s
#             else:
#                 return s[0]
#         else:
#             # 峰顶为相同两数的回文串 长度为偶数
#             first_length = 0
#             second_length = 0
#             first_peak = 0
#             second_peak = 0
#             in_first = False
#             in_second = False
#             # 峰顶为一个数的回文串 长度为奇数
#             first_length_tr = 0
#             second_length_tr = 0
#             first_peak_tr = 0
#             second_peak_tr = 0
#             in_first_tr = False
#             in_second_tr = False
#             # 最长相同字符相连子串
#             same_length = 0
#             same_start_index = 0
#             next_same_length = 0
#             next_start_index = 0
#             in_next_same = False
#             # 维持一个当前最长串为first串，通过second串探索来更新当前最长串first串的状态
#             for i, c in enumerate(s[1:]):
#                 i = i + 1
#                 # 若second回文串长度超过目前最长的回文串first串，让second串归零开始探索下一个可能的最长串
#                 # 将second串的状态复制到first串上
#                 if second_length > first_length:
#                     first_length = second_length
#                     first_peak = second_peak
#                     second_length = 0
#                     in_second = False
#                     in_first = True
#                 if second_length_tr > first_length_tr:
#                     first_length_tr = second_length_tr
#                     first_peak_tr = second_peak_tr
#                     second_length_tr = 0
#                     in_second_tr = False
#                     in_first_tr = True
#                 # 如果second串不为零说明second已被创建且正在探索下一个新最长串
#                 # 按条件更新second串，若不满足条件则将second归零，待之后再创建second串继续探索
#                 if second_length != 0 and in_second:
#                     if s[i] == s[i - second_length - 1] and i - second_length - 1 >= 0:
#                         second_length += 2
#                     else:
#                         in_second = False
#                         second_length = 0
#                 if second_length_tr != 0 and in_second_tr:
#                     if s[i] == s[i - second_length_tr - 1] and i - second_length_tr - 1 >= 0:
#                         second_length_tr += 2
#                     else:
#                         in_second_tr = False
#                         second_length_tr = 0
#                 # 如果first串不为零且first串在伸长中，按条件更新first串，若不在伸长中，则等待second串探索来进行更新
#                 if first_length != 0 and in_first:
#                     if s[i] == s[i - first_length - 1] and i - first_length - 1 >= 0:
#                         first_length += 2
#                     else:
#                         in_first = False
#                 if first_length_tr != 0 and in_first_tr:
#                     if s[i] == s[i - first_length_tr - 1] and i - first_length_tr - 1 >= 0:
#                         first_length_tr += 2
#                     else:
#                         in_first_tr = False
#                 # 若满足回文条件探索串长度正为零，则需开启一个新串
#                 if s[i] == s[i - 1]:
#                     if second_length == 0:
#                         second_peak = i - 1
#                         second_length = 2
#                         in_second = True
#                     if not in_next_same:
#                         next_same_length = 2
#                         next_start_index = i - 1
#                         in_next_same = True
#                     else:
#                         if next_start_index + next_same_length == i:
#                             next_same_length += 1
#                         else:
#                             next_same_length = 2
#                             next_start_index = i - 1
#                             in_next_same = True
#                         if same_length < next_same_length:
#                             same_length = next_same_length
#                             same_start_index = next_start_index
#                 if s[i] == s[i - 2] and i > 1:
#                     if second_length_tr == 0:
#                         second_peak_tr = i - 1
#                         second_length_tr = 3
#                         in_second_tr = True
#             if first_length < second_length:
#                 first_peak = second_peak
#                 first_length = second_length
#             if first_length_tr < second_length_tr:
#                 first_length_tr = second_length_tr
#                 first_peak_tr = second_peak_tr
#
#             if first_length == first_length_tr == same_length == 0:
#                 return s[0]
#             elif first_length > first_length_tr and first_length >= same_length:
#                 return s[first_peak - int(first_length / 2) + 1:first_peak + int(first_length / 2) + 1]
#             elif first_length_tr > first_length and first_length_tr >= same_length:
#                 return s[first_peak_tr - int(first_length_tr / 2):first_peak_tr + int(first_length_tr / 2) + 1]
#             else:
#                 return s[same_start_index:same_start_index + same_length]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        max_l = 0
        max_r = 0

        for r in range(1, len(s)):
            for l in range(0, r):
                if l == r - 1 and s[l] == s[r]:
                    dp[l][r] = True
                if dp[l+1][r-1] and s[l] == s[r]:
                    dp[l][r] = True
                if dp[l][r]:
                    if r - l > max_r - max_l:
                        max_l = l
                        max_r = r

        return s[max_l: max_r+1]




a = 'abababababababa'
solution = Solution()
print(solution.longestPalindrome(a))

