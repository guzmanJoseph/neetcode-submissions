class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            chars = {}
            for i in range(len(word)):
                if word[i] in chars:
                    chars[word[i]] += 1
                else:
                    chars[word[i]] = 1
            
            key = tuple(sorted(chars.items()))

            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]

        return list(result.values())

            

        
        