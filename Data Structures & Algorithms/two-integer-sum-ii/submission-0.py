class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers[i+1:]:
                output.append(i+1)
                output.append(numbers.index((target - numbers[i]))+1)
        return output


        