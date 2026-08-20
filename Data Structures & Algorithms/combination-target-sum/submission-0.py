class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(i, current_sum):
            if current_sum == target:
                result.append(path.copy())
                return 
            
            if current_sum > target:
                return

            if i == len(nums):
                return
            path.append(nums[i])
            backtrack(i, current_sum + nums[i])

            path.pop()

            backtrack(i+1, current_sum)

        backtrack(0, 0)
        return result
        