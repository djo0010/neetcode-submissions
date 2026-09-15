class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currMax = 0
        currChars = set()
        l = 0
        for r in range(len(s)):
            if s[r] not in currChars:
                currChars.add(s[r])
            else:
                while s[l] != s[r]:
                    currChars.remove(s[l])
                    l += 1
                currChars.remove(s[l])
                l += 1
                currChars.add(s[r])
            currMax = max(currMax, r - l + 1)
        return currMax


