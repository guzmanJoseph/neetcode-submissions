class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1
        result = 0
        left = 0
        right = 1
        chars = set()
        chars.add(s[left])

        while right != len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1
                current_result = right - left
                result = max(result, current_result)
        return result