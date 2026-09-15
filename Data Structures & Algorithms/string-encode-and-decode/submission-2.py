class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += self.processString(s)
        return res

    def processString(self, string: str):
        if len(string) >= 100:
            return f"${len(string)}{string}"
        if len(string) >= 10:
            return f"%{len(string)}{string}"
        return f"#{len(string)}{string}"


    def decode(self, s: str) -> List[str]:
        res = []
        count = -1
        i = 0
        wordLength = -1
        while i < len(s):
            #capture leading elements and count
            if s[i] == "#":
                wordLength = int(s[i + 1])
                wordStart = i + 2

            elif s[i] == "%":
                wordLength = int(s[i+1:i+3]) 
                wordStart = i + 3

            elif s[i] == "$":
                wordLength = int(s[i+1:i+4])
                wordStart = i + 4
            
            #capture word
            word = s[wordStart:wordStart + wordLength]

            res.append(word)

            i = wordStart + wordLength

        return res



            

        