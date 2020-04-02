from typing import List

from algorithm.leetcode.model import TrieNode


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        root = TrieNode('')
        curr = root
        ans = strs[0]

        for i in range(0, len(strs)):
            word = strs[i]
            prefix = 0
            flag = False
            for j in range(0, len(word)):
                if curr.childrens[ord(word[j]) - ord('a')] is None:
                    curr.childrens[ord(word[j]) - ord('a')] = TrieNode('')
                    flag = True
                if flag == False or i == 0:
                    prefix = prefix + 1
                curr = curr.childrens[ord(word[j]) - ord('a')]
            if prefix <= len(ans):
                ans = word[0:prefix]
            curr = root

        return ans

    def longestCommonPrefixC(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        ans = strs[0]
        for s in strs:
            for i in range(0, len(ans)):
                if i >= len(s) or s[i] != ans[i]:
                    ans = ans[0:i]
                    break

        return ans


if __name__ == "__main__":
    solution = Solution()
    # strs = ["flower", "flow", "flight"]
    strs = ["aa", "a"]
    print(solution.longestCommonPrefixC(strs))
