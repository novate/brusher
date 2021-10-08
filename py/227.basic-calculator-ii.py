from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        q = deque()
        op_1 = ('+', '-')
        op_2 = ('*', '/')
        i = 0
        prev_num_str = ''
        while i < len(s):
            if s[i] in op_1:
                q.append(int(prev_num_str.strip()))
                q.append(s[i])
                prev_num_str = ''
            elif s[i] in op_2:
                op = s[i]
                num_1 = int(prev_num_str)
                prev_num_str = ''
                i += 1
                while i < len(s) and s[i] not in op_1 and s[i] not in op_2:
                    prev_num_str += s[i]
                    i += 1
                num_2 = int(prev_num_str.strip())
                if op == '*':
                    prev_num_str = str(num_1 * num_2)
                else:
                    prev_num_str = str(num_1 // num_2)

                i -= 1
            elif s[i] not in op_1 and s[i] not in op_2:
                prev_num_str += s[i]
            i += 1

        if len(prev_num_str) > 0:
            q.append(int(prev_num_str))

        while len(q) >= 3:
            num_1 = q.popleft()
            op = q.popleft()
            num_2 = q.popleft()
            if op == '+':
                q.appendleft(num_1 + num_2)
            else:
                q.appendleft(num_1 - num_2)

        return q.pop()
