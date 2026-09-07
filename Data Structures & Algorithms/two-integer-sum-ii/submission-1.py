class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            sumtwo = numbers[left] + numbers[right]
            if  sumtwo == target:
                return [left+1, right+1]
            elif sumtwo > target:
                right -= 1
            elif sumtwo < target:
                left += 1
            


        