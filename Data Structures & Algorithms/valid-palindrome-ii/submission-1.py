class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.isValidPalindrome(s[l:r]) or self.isValidPalindrome(s[l+1:r+1])
            l += 1
            r -= 1
        return True


    def isValidPalindrome(self, s: str) -> bool:
        print(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True