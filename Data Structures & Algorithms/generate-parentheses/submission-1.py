class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_bracket = 0
        close_bracket = 0
        path = []
        result = []

        def backtrack(open_bracket, close_bracket):
            if close_bracket > open_bracket:
                return

            if len(path) == 2 * n:
                result.append("".join(path))
                return

            if open_bracket < n:
                path.append("(")
                backtrack(open_bracket + 1, close_bracket)
                path.pop()

            if close_bracket < open_bracket:
                path.append(")")
                backtrack(open_bracket, close_bracket + 1)
                path.pop()

        backtrack(0,0)
        return result


             

            
        