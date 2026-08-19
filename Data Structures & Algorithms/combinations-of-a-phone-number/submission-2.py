class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(i, s):
            nonlocal res
            if i == len(digits):
                print(s)
                res.append(s)
                return
            for c in phone[digits[i]]:
                s = s + c
                backtrack(i + 1, s)
                s = s[:-1]
            return

        backtrack(0, "")

        return res