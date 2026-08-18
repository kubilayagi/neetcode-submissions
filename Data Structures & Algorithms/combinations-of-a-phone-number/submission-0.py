class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        stack = []
        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def dfs(i):
            nonlocal res
            nonlocal stack
            if len(stack) == len(digits):
                res.append(''.join(stack))
                return
            if len(stack) > len(digits):
                return
            curLetters = letters[digits[i]]
            for l in curLetters:
                stack.append(l)
                dfs(i+1)
                stack.pop()

        dfs(0)
        return res