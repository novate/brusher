class Solution:
    def reverseWords(self, s: str) -> str:
        q = []
        raw_split = s.split(' ')
        for raw_w in raw_split:
            w = raw_w.strip()
            if w:
                q.append(w)

        return ' '.join(q[::-1])
