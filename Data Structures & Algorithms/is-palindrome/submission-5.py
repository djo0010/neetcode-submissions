import re

class Solution:

    
    def make_alphanum(self, s: str) -> str:
        return re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
    def isPalindrome(self, s: str) -> bool:
        s = self.make_alphanum(s)

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
