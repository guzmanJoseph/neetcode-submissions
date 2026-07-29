class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        result = []
        for index, num in enumerate(nums):
            difference = target - nums[index]
            if difference in dictionary:
                result.append(dictionary[difference])
                result.append(index)
            dictionary[num] = index
        return result