class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        left = 0
        right = 0

        def backtrack(start):
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start, len(s)):
                substring = s[start: end + 1]

                if substring == substring[::-1]:
                    path.append(substring)

                    backtrack(end+1)

                    path.pop()

        backtrack(0)
        return result
        