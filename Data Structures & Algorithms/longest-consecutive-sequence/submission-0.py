class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        con  = {}
        start = 0
        for index in range(len(s)-1):
            length = index - start + 1
            if (s[index] + 1) != s[index+1]:
                con[start] = length
                start = index + 1
            con[start] = length + 1
        return max(con.values())

        