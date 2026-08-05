class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            current_max = (right - left) * min(heights[left], heights[right])

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            max_area = max(max_area, current_max)

        return max_area
        