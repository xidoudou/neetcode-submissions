class Solution:

    def isValid(self, s: str) -> bool:
        bdict = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
        braces = []
        for l in s:
            if l in "({[":
                braces.append(l)
            else:
                if not braces or braces.pop() != bdict[l]:
                    return False
        
        return len(braces) == 0
        
        
        
