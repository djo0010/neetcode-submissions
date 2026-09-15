class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        counts = {}
        for i in s:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        for j in t:
            if j in counts:
                counts[j] -= 1
            else:
                return False
        if all(value == 0 for value in counts.values()):
            return True
        else:
            return False
