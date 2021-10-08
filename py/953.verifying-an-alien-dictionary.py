from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ch_idx = {ch: idx for idx, ch in enumerate(order)}
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if ch_idx[words[i][j]] > ch_idx[words[i+1][j]]:
                        return False
                    break
        return True
