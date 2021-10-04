from typing import List


class Solution:
    def merge_1(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key=lambda e: e[0])
        print(intervals)
        ans = []
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] <= cur_end:
                cur_end = max(cur_end, interval[1])
            else:
                ans.append([cur_start, cur_end])
                cur_start = interval[0]
                cur_end = interval[1]
        ans.append([cur_start, cur_end])
        return ans

        # Follow-up: no sorting
