class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {']':'[', '}':'{', ')':'('}

        if len(s) % 2 != 0:
            return False
        
        for character in s:
            if character in mappings.keys():
                if len(stack) == 0 or mappings[character] != stack.pop():
                    return False
            else:
                stack.append(character)
        return len(stack) == 0
