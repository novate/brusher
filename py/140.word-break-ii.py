from collections import deque


class SolutionBFS:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        q = deque([0])
        jumpers = {}

        while q:
            start = q.popleft()
            if start in jumpers:
                continue
            jumpers[start] = set()
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_set:
                    jumpers[start].add(end)
                    q.append(end)

        paths = {0: [[0]]}

        for start in range(len(s)):
            if start not in jumpers:
                continue
            ends = jumpers[start]
            for end in ends:
                if end not in paths:
                    paths[end] = []
                for path in paths[start]:
                    paths[end].append(path + [end])

        if len(s) not in paths:
            return []

        outputs = []
        for path in paths[len(s)]:
            outputs.append(' '.join([s[path[idx]:path[idx+1]]
                           for idx in range(len(path)-1)]))
        return outputs
