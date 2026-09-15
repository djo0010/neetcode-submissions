class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
             match token:
                case "*":
                    stack.append(int(stack.pop() * stack.pop()))
                case "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b - a))                
                case "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
                case "+":    
                    stack.append(int(stack.pop() + stack.pop()))
                case _:  
                    stack.append(int(token))
        return stack[0]