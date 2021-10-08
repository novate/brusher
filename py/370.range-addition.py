from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0 for _ in range(length)]

        for update in updates:
            arr[update[0]] += update[2]
            if update[1] + 1 < length:
                arr[update[1]+1] -= update[2]

        for idx in range(1, length):
            arr[idx] += arr[idx-1]

        return arr
