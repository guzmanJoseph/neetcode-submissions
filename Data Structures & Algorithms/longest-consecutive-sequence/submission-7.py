class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 0:
            return 0

        longest = 1
        current = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+ 1] - 1:
                current += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)
        