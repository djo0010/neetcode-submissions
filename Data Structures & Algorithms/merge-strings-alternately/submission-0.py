class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        w1 = 0
        w2 = 0

        s = []
        
        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1) and w2 >= len(word2):
                s += word1[w1: len(word1)]
                break
            elif w1 >= len(word1) and w2 < len(word2):
                s += word2[w2: len(word2)]
                break
            else:
                s.append(word1[w1])
                s.append(word2[w2])
                w1 += 1
                w2 += 1
        return "".join(s)
