from typing import List
from collections import deque


class SolutionMemoization:
    def __init__(self):
        self.word_set = set()
        self.ans_hash = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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


class SolutionBFS:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
                visited.add(start)
        return False


class SolutionDP:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
