from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(0, s, [], ans)
        return ans

    def dfs(self, begin: int, s: str, tmp: List[str], ans: List[str]):
        if len(tmp) == 4:
            if begin < len(s):
                return
            for i in range(0, 4):
                if int(tmp[i]) > 255 or (int(tmp[i]) == 0 and tmp[i] != "0") or (tmp[i][0] == "0" and int(tmp[i]) != 0):
                    return
            ans.append(".".join(tmp))

        for i in range(1, 4):
            if begin + i > len(s):
                continue
            tmp.append(s[begin:begin + i])
            self.dfs(begin + i, s, tmp, ans)
            tmp.pop()
