class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        bad_i = set()
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append((i, ch))
            if ch == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    bad_i.add(i)
        while len(stack) > 0:
            i, ch = stack.pop()
            bad_i.add(i)
        ans = ''
        for i in range(len(s)):
            if i not in bad_i:
                ans += s[i]
        return ans
