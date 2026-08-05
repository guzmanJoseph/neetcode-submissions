class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                firstNum = stack.pop()
                secondNum = stack.pop()
                
                if token == '+':
                    result = int(firstNum) + int(secondNum)

                elif token == '-':
                    result = int(secondNum) - int(firstNum)

                elif token == '*':
                    result = int(firstNum) * int(secondNum)

                elif token == '/':
                    result = int(secondNum) / int(firstNum)

                stack.append(int(result))

        return stack[-1]
                
            
        