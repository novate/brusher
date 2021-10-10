from random import randint
from typing import List
import heapq


class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class SolutionQuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, len(nums)-k, 0, len(nums)-1)

    def quickSelect(self, nums, k, l, r):
        if l < r:
            pivot = self.partition(nums, l, r)
            if pivot == k:
                return nums[pivot]
            elif pivot > k:
                return self.quickSelect(nums, k, l, pivot-1)
            else:
                return self.quickSelect(nums, k, pivot+1, r)
        else:
            return nums[k]

    def partition(self, nums, l, r):
        rnd = randint(l, r)
        nums[rnd], nums[r] = nums[r], nums[rnd]
        pivot = r
        while l < r:
            while l < r and nums[l] < nums[pivot]:
                l += 1
            while l < r and nums[r] >= nums[pivot]:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        nums[r], nums[pivot] = nums[pivot], nums[r]
        return r
