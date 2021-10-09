from typing import List


class Solution:
    def __init__(self):
        self.word_set = set()
        self.ans_hash = {}

    def wordBreakMemoization(self, s: str, wordDict: List[str]) -> bool:
        if len(self.word_set) == 0:
            self.word_set = set(wordDict)
        if s in self.word_set:
            return True
        results = []
        for i in range(1, len(s)):
            if s[:i] not in self.word_set:
                results.append(False)
            elif len(s) in self.ans_hash:
                results.append(self.ans_hash[len(s)])
            else:
                results.append(self.wordBreak(s[i:], wordDict))
        result = any(results)
        self.ans_hash[len(s)] = result

        return result
