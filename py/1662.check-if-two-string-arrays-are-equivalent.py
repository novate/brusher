from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        p1 = 0
        p2 = 0
        cw1 = word1[p1]
        cw2 = word2[p2]
        while p1 < len(word1) and p2 < len(word2):
            l1 = len(cw1)
            l2 = len(cw2)
            if l1 == l2:
                if cw1 != cw2:
                    return False
                else:
                    p1 += 1
                    p2 += 1
                    if p1 < len(word1):
                        cw1 = word1[p1]
                    if p2 < len(word2):
                        cw2 = word2[p2]
            elif l1 < l2:
                if cw1 != cw2[:l1]:
                    return False
                else:
                    p1 += 1
                    if p1 < len(word1):
                        cw1 = word1[p1]
                    cw2 = cw2[l1:]
            else:
                if cw2 != cw1[:l2]:
                    return False
                else:
                    cw1 = cw1[l2:]
                    p2 += 1
                    if p2 < len(word2):
                        cw2 = word2[p2]
        if p1 != len(word1) or p2 != len(word2):
            return False
        return True
