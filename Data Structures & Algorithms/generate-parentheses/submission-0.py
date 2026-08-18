class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def dfs(openParens, closedParens):
            nonlocal stack
            if openParens == closedParens == n:
                res.append(''.join(stack.copy()))
                return
            if closedParens > openParens:
                return
            if openParens > n or closedParens > n:
                return

            stack.append('(')
            dfs(openParens + 1, closedParens)
            stack.pop()
            stack.append(')')
            dfs(openParens, closedParens + 1)
            stack.pop()

        dfs(0, 0)
        return res
            