from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bisect(nums, target, 0, len(nums))

    def bisect(self, nums, target, l, r):
        if l == r:
            return -1
        if r == l+1:
            return l if nums[l] == target else -1
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        section_sorted = nums[l] < nums[r-1]
        if section_sorted:
            if nums[mid] < target:
                return self.bisect(nums, target, mid+1, r)
            else:
                return self.bisect(nums, target, l, mid)
        search_left = self.bisect(nums, target, mid+1, r)
        if search_left != -1:
            return search_left
        else:
            return self.bisect(nums, target, l, mid)
