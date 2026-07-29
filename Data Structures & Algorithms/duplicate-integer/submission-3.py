class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dups = set()
        for num in nums:
            no_dups.add(num)
        
        if len(no_dups) != len(nums):
            return True
        return False