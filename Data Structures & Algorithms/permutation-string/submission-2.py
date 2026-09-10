class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        for char in s1:
            s1Count[char] = s1Count.get(char,0) + 1
        
        tmp = {}
        l = 0
        for r in range(len(s2)):

            if s2[r] not in s1Count:
                l = r + 1
            else:
                tmp[s2[r]] = tmp.get(s2[r], 0) + 1
            
            if tmp == s1Count:
                return True

        return False

                

        