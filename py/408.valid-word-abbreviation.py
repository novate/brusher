class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        lw = len(word)
        labbr = len(abbr)
        w_ptr = 0
        a_ptr = 0
        w_num = ""
        while w_ptr < lw and a_ptr < labbr:
            while a_ptr < labbr and abbr[a_ptr].isnumeric():
                if len(w_num) == 0 and abbr[a_ptr] == '0':
                    return False
                w_num += abbr[a_ptr]
                a_ptr += 1
            if len(w_num) > 0:
                w_ptr += int(w_num)
                if w_ptr >= lw:
                    return w_ptr == lw and a_ptr == labbr
                w_num = ""
                continue
            if abbr[a_ptr].isalpha():
                if abbr[a_ptr] != word[w_ptr]:
                    print('w2')
                    return False
                a_ptr += 1
                w_ptr += 1
        return w_ptr == lw and a_ptr == labbr
