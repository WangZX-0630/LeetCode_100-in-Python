from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for i in range(len(strs)):
            flag = 0
            characters = []
            for c in strs[i]:
                characters.append(c)
            characters.sort()
            characters = ''.join([str(s) for s in characters])
            for k in result_dict.keys():
                if characters == k:
                    result_dict[characters].append(strs[i])
                    flag = 1
                    break
            if flag == 0:
                result_dict[characters] = [strs[i]]
        return list(result_dict.values())


if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))
