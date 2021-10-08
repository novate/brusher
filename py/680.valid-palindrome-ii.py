class Solution:
    no_remove = True

    def validPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1
        no_remove = True
        while lp < rp:
            if s[lp] == s[rp]:
                lp += 1
                rp -= 1
            elif self.no_remove:
                self.no_remove = False
                return self.validPalindrome(s[lp:rp]) or self.validPalindrome(s[lp+1:rp+1])
            else:
                return False
        return True
