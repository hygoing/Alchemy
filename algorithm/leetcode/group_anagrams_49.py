from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in dict:
                dict[sort_s].append(s)
            else:
                dict[sort_s] = [s]
        return list(dict.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            keys = [0] * 26
            for ch in s:
                keys[ord(ch) - ord('a')] += 1
            key = "".join(str(i) for i in keys)
            if key in dict:
                dict[key].append(s)
            else:
                dict[key] = [s]
        return list(dict.values())


if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))
