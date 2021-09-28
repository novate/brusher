from typing import List


class Solution:
    def trap_double_list(self, height: List[int]) -> int:
        left_highs = [0] * len(height)
        for idx in range(0, len(height)-1):
            left_highs[idx+1] = max(left_highs[idx], height[idx])
        right_highs = [0] * len(height)
        for idx in range(len(height)-1, 0, -1):
            right_highs[idx-1] = max(right_highs[idx], height[idx])
        water_line = [min(left_highs[i], right_highs[i])
                      for i in range(len(height))]
        ans = 0
        for idx, h in enumerate(height):
            if h < water_line[idx]:
                ans += water_line[idx] - h
        return ans

    def trap_double_ptr(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        left_ptr = 0
        right_ptr = len(height) - 1
        ans = 0
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                if height[left_ptr] > left_max:
                    left_max = height[left_ptr]
                else:
                    ans += left_max - height[left_ptr]
                left_ptr += 1
            else:
                if height[right_ptr] > right_max:
                    right_max = height[right_ptr]
                else:
                    ans += right_max - height[right_ptr]
                right_ptr -= 1
        return ans
