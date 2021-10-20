class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        num1, num2 = num1.zfill(n), num2.zfill(n)

        ans = []

        carry = 0
        for i in range(n-1, -1, -1):
            carry += int(num1[i])
            carry += int(num2[i])
            ans.append(str(carry % 10))
            carry //= 10

        if carry != 0:
            ans.append(str(carry))

        return ''.join(ans[::-1])
