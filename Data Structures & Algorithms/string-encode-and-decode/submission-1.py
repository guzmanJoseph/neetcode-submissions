class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result  += str(len(word)) + "#" + word 
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        left = 0

        while i < len(s):
            left = i

            while s[left] != "#":
                left += 1
            
            length = int(s[i:left])
            word = s[left + 1: left + length + 1]
            result.append(word)
            i = left + 1 + length

        return result