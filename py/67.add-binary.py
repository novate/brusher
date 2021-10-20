class SolutionBitByBit:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

        if carry == 1:
            answer.append('1')

        return ''.join(answer[::-1])


class SolutionBitManipulation:
    def addBinary(self, a: str, b: str) -> str:
        a_int, b_int = int(a, 2), int(b, 2)
        while b_int:
            plus = a_int ^ b_int
            carry = (a_int & b_int) << 1
            a_int, b_int = plus, carry
        return bin(a_int)[2:]
