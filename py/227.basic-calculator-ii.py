from collections import deque


class SolutionStack:
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


class SolutionLastNum:
    def calculate(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0

        signs = {'+', '-', '*', '/'}
        cur_num = 0
        last_num = 0
        result = 0
        prev_sign = '+'
        for i in range(length):
            cur_char = s[i]
            if cur_char.isdigit():
                cur_num *= 10
                cur_num += int(cur_char)
            if cur_char in signs or i == length-1:
                if prev_sign == '+' or prev_sign == '-':
                    result += last_num
                    last_num = cur_num if prev_sign == '+' else -cur_num
                elif prev_sign == '*':
                    last_num *= cur_num
                elif prev_sign == '/':
                    if last_num < 0:
                        last_num = -(-last_num // cur_num)
                    else:
                        last_num //= cur_num
                prev_sign = cur_char
                cur_num = 0
        return result + last_num
