class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        cur = x

        i = n
        while i > 0:
            if i % 2 == 1:
                ans *= cur
            cur *= cur
            i //= 2
        return ans
