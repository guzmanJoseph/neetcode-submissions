class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = {}
        for i in range(len(s1)):
            if s1[i] in s1_dict:
                s1_dict[s1[i]] += 1
            else:
                s1_dict[s1[i]] = 1
        
        left = 0
        s2_dict = {}
        for right in range(len(s2)):
            if s2[right] in s2_dict:
                s2_dict[s2[right]] += 1
            else:
                s2_dict[s2[right]] = 1
            
            current_window = right - left + 1
            if current_window > len(s1):
                s2_dict[s2[left]] -= 1
                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]
                left += 1
            if (right - left + 1) == len(s1) and s1_dict == s2_dict:
                return True
        return False
            

