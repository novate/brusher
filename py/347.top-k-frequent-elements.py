from random import randint
from typing import List


class SolutionQuickSelect:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        keys = list(counter.keys())
        self.quickSelect(counter, keys, k-1, 0, len(keys)-1)
        return keys[:k]

    def quickSelect(self, counter, keys, k, l, r):
        if l < r:
            pivot = self.partition(counter, keys, l, r)
            if pivot == k:
                return
            elif pivot > k:
                self.quickSelect(counter, keys, k, l, pivot-1)
            else:
                self.quickSelect(counter, keys, k, pivot+1, r)
        else:
            return

    def partition(self, counter, keys, l, r):
        rnd = randint(l, r)
        keys[rnd], keys[r] = keys[r], keys[rnd]
        pivot = r
        while l < r:
            while l < r and counter[keys[l]] > counter[keys[pivot]]:
                l += 1
            while l < r and counter[keys[r]] <= counter[keys[pivot]]:
                r -= 1
            keys[l], keys[r] = keys[r], keys[l]
        keys[r], keys[pivot] = keys[pivot], keys[r]
        return r
