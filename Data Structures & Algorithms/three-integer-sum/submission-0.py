class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        number = sorted(nums)
        n = len(number)
        for i in range(n):
            if i > 0 and number[i] == number[i-1]:
                continue
            if number[i] > 0:
                break
            if i + 2 < n and number[i] +number[i+1] + number[i+2] > 0:
                break
            left = i + 1
            right = n - 1
            while left < right:
                sumthree = number[i] + number[left] + number[right]
                if sumthree == 0:
                    output.append([number[i],number[left],number[right]])
                    left += 1
                    right -= 1
                    while left < right and number[left] == number[left-1]:
                        left += 1
                    while left < right and number[right] == number[right+1]:
                        right -= 1
                elif sumthree < 0:
                    left += 1
                else:
                    right -= 1
        return output
            


        