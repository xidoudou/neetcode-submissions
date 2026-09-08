from collections import deque
class Solution:

    def isValid(self, s: str) -> bool:
        bdict = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
        braces = deque()
        for l in s:
            if l in "({[]})":
                braces.append(l)
        while braces:
            if bdict[braces.pop()] != braces.popleft():
                return False
            if len(braces) == 1:
                return False
        return True
        
        
        
