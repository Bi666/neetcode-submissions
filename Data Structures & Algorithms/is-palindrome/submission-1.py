class Solution:
    def is_ascii(self, char: str) -> bool:
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')
    
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            while i <= j and not self.is_ascii(s[i]):
                i += 1
            while i <= j and not self.is_ascii(s[j]):
                j -= 1
            if i <= j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
