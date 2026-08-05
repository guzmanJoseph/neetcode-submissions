class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }


        for i in range(len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == "[":
                stack.append(s[i])

            else:
                if not stack:
                    return False

                if s[i] in '})]' and stack[-1] != pairs[s[i]]:
                    return False

                stack.pop()
        return len(stack) == 0


        