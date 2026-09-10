class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        template = Counter(s1)

        l = 0
        for r in range(len(s1)-1, len(s2)):
            if Counter(s2[l:r+1]) == template:
                return True
            l += 1
        return False

