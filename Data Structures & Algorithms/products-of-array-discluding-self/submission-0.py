class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [] # this is what we are returning
        prefix = [1]
        suffix = [1]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i-1])

        for i in range(len(nums) - 2, -1, -1):
            suffix.append(suffix[-1] * nums[i+1])

        suffix.reverse()

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result
