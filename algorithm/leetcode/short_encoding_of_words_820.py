from typing import List

from algorithm.leetcode.model import TrieNode


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ans = 0
        root = TrieNode("")
        curr = root
        words.sort(key=lambda x: len(x))

        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            flag = False
            for j in range(len(word) - 1, -1, -1):
                if curr.childrens[ord(word[j]) - ord('a')] is None:
                    curr.childrens[ord(word[j]) - ord('a')] = TrieNode('')
                    flag = True
                curr = curr.childrens[ord(word[j]) - ord('a')]

            incr = len(word) + 1 if flag else 0
            ans = ans + incr
            curr = root
        return ans


if __name__ == "__main__":
    words = ["me", "time"]
    solution = Solution()
    print(solution.minimumLengthEncoding(words))
