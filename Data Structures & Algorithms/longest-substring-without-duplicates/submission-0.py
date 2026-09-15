class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currMax = 0
        currChars = set()
        l = 0
        for r in range(len(s)):
            print("Iteration r", currChars, s[l:r+1])
            if s[r] not in currChars:
                currChars.add(s[r])
                print("Regular add r", currChars, s[l:r+1])                
            else:
                print("s[r] in chars", s[r])
                while s[l] != s[r]:
                    currChars.remove(s[l])
                    l += 1
                currChars.remove(s[l])
                l += 1
                currChars.add(s[r])
            currMax = max(currMax, r - l + 1)
        
        return currMax


