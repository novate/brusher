from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        s = 0
        h = {0: 1}
        for num in nums:
            s += num
            if s - k in h:
                cnt += h[s-k]
            if s in h:
                h[s] += 1
            else:
                h[s] = 1
        return cnt
