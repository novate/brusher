from typing import List
from random import randint


class SolutionQuickSortOnePtr:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums: List[int], lower, upper):
        if lower >= upper:
            return

        pivot = randint(lower, upper)
        nums[pivot], nums[upper] = nums[upper], nums[pivot]
        pivot = self.partition(nums, lower, upper)
        self.quickSort(nums, lower, pivot-1)
        self.quickSort(nums, pivot+1, upper)

    def partition(self, nums: List[int], lower, upper):
        i = lower
        pivot = nums[upper]

        for j in range(lower, upper):
            if nums[j] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1

        nums[i], nums[upper] = nums[upper], nums[i]
        return i


class SolutionQuickSortDoublePtr:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, l, r):
        if l < r:
            rnd = randint(l, r)
            nums[rnd], nums[r] = nums[r], nums[rnd]
            p = self.partition(nums, l, r)
            self.quickSort(nums, l, p-1)
            self.quickSort(nums, p+1, r)

    def partition(self, nums, l, r):
        pivot = r
        while l < r:
            while l < r and nums[l] < nums[pivot]:
                l += 1
            while l < r and nums[r] >= nums[pivot]:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        nums[r], nums[pivot] = nums[pivot], nums[r]
        return r


class SolutionMerge:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        nums_1 = self.sortArray(nums[:mid])
        nums_2 = self.sortArray(nums[mid:])
        return self.merge(nums_1, nums_2)

    def merge(self, nums_1, nums_2):
        nums = []
        i = 0
        j = 0
        while i < len(nums_1) and j < len(nums_2):
            if nums_1[i] < nums_2[j]:
                nums.append(nums_1[i])
                i += 1
            else:
                nums.append(nums_2[j])
                j += 1
        if i != len(nums_1):
            nums += nums_1[i:]
        if j != len(nums_2):
            nums += nums_2[j:]
        return nums
