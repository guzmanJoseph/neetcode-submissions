class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(i, current_sum):
            if current_sum == target:
                result.append(path.copy())
                return

            if current_sum > target:
                return

            if i == len(candidates):
                return

            path.append(candidates[i])
            backtrack(i+1, current_sum + candidates[i])

            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i+1, current_sum)

        backtrack(0,0)
        return result
        