from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if i == 0:
                new_nums = nums[1:]
            elif i == len(nums)-1:
                new_nums = nums[0:i]
            else:
                new_nums = nums[0:i] + nums[i+1:]
            result.append(prod(new_nums))
        return result

        