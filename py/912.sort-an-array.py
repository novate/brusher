from typing import List
from random import randint


class SolutionQuickSort:
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
