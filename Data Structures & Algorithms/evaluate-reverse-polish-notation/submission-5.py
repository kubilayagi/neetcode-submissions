class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            if t.isnumeric() or (t.startswith('-') and t[1:].isnumeric()):
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                if t == "+":
                    stack.append(x + y)
                elif t == "-":
                    stack.append(x - y)
                elif t == "*":
                    stack.append(x * y)
                elif t == "/":
                    stack.append(int(x / y))

        return stack.pop()
