from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        self.reverse(nums, i+1)

    def reverse(self, nums: List[int], start: int) -> None:
        i = start
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


class MySolution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find from back to front the longest DESC array stopping at a certain idx
        idx = len(nums) - 2
        while idx >= 0:
            if nums[idx] >= nums[idx+1]:
                idx -= 1
            else:
                break
        # if idx is valid, find from front to back the closest number to back
        if idx >= 0:
            j = idx+1
            while j < len(nums):
                if nums[j] > nums[idx]:
                    j += 1
                else:
                    break
            # swap these two numbers
            if j-1 != len(nums):
                nums[idx], nums[j-1] = nums[j-1], nums[idx]
        # change DESC to ASC
        self.rev(nums, idx+1)

    def rev(self, nums: List[int], idx: int) -> None:
        front = idx
        back = len(nums) - 1
        while front < back:
            nums[front], nums[back] = nums[back], nums[front]
            front += 1
            back -= 1
