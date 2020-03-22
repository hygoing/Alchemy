class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        if len(s) == 0:
            return True

        stack = []
        for ch in s:
            if len(stack) > 0 and self.isRightBracket(ch):
                matched = self.matchBracket(stack[-1], ch)
                if matched == False:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        if len(stack) > 0 :
            return False

        return True

    def matchBracket(self, s1: str, s2: str) -> bool:
        if s1 == "(" and s2 == ")" or s1 == "[" and s2 == "]" or s1 == "{" and s2 == "}":
            return True
        return False

    def isRightBracket(self, s: str) -> bool:
        if s == ")" or s == "]" or s == "}":
            return True
        return False


if __name__ == "__main__":
    s = "{[}]"

    solution = Solution()
    print(solution.isValid(s))
