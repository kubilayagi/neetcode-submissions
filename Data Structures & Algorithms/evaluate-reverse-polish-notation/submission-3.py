class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        stack.append(int(tokens[0]))
        stack.append(int(tokens[1]))
        i = 2
        while i < len(tokens):
            while tokens[i] not in ['+', '-', '*', '/']:
                stack.append(int(tokens[i]))
                i+=1
            op = tokens[i]
            a = stack.pop()
            b = stack.pop()
            if op == '+':
                stack.append(a + b)
            elif op == '-':
                stack.append(b - a)
            elif op == '*':
                stack.append(a * b)
            elif op == '/':
                stack.append(int(b / a))
            i+=1
        res = stack.pop()
        return res