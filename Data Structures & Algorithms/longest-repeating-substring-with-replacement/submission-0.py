class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars_dict = {}
        result = 0
        left = 0

        for right in range(len(s)):
            if s[right] in chars_dict:
                chars_dict[s[right]] += 1
            else:
                chars_dict[s[right]] = 1

            num_replacements = (right - left + 1) - max(chars_dict.values())
            while num_replacements > k:
                chars_dict[s[left]] -= 1
                left += 1
                num_replacements = (right - left + 1) - max(chars_dict.values())
            
            result = max(result, right - left + 1)
        return result
            


            

        
        