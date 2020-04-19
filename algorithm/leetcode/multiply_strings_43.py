class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        products = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                products[i + j + 1] += int(num1[i]) * int(num2[j])
        carry = 0
        for i in range(len(products) - 1, -1, -1):
            products[i] += carry
            carry = products[i] // 10
            products[i] %= 10

        print(products)
        i = 0
        while i < len(products) - 1 and products[i] == 0:
            i += 1

        ans = ""
        for j in range(i, len(products)):
            ans += str(products[j])

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply("123", "456"))

