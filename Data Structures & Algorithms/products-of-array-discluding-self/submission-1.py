from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        running_product = 1
        for num in nums:
            prefix.append(running_product)
            running_product *= num
        suffix = [1] * len(nums)
        running_product = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = running_product 
            running_product *= nums[i]

        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result


            



        