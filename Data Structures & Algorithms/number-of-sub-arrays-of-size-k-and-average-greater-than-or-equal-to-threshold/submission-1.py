class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        result = 0
        window_sum = 0
        for right in range(len(arr)):
            window_sum += arr[right]
            window_size = right - left + 1

            if window_size > k:
                window_sum -= arr[left]
                left += 1

            if right - left + 1 == k and (window_sum) / k >= threshold:
                result += 1
            
        return result
        