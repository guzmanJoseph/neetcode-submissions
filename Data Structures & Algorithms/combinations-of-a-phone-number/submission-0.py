class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        current_string = []
        result = []

        def backtrack(i):
            if i == len(digits):
                result.append("".join(current_string))
                return

            for letter in dic[digits[i]]:
                current_string.append(letter)

                backtrack(i+1)

                current_string.pop()

        backtrack(0)
        return result



            



        