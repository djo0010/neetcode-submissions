class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    stack.append(stack[len(stack)-1] + stack[len(stack) - 2])
                case "D":
                    print("double", stack[len(stack)-1] * 2)
                    stack.append(stack[len(stack)-1]*2)
                case "C":
                    print("remove", stack[len(stack)-1])                    
                    stack.pop()
                case _:
                    stack.append(int(operations[i]))
            print(stack)
        return sum(stack)