class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []
        
        def isPalindrome(test):
            i, j = 0, len(test) - 1
            while i < j:
                if test[i] != test[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(l, r):
            nonlocal res
            nonlocal stack
            if len(''.join(stack)) == len(s):
                res.append(stack.copy())
            if r >= len(s):
                return
            origL = l
            origR = r
            nextL = r + 1
            nextR = nextL
            if isPalindrome(s[l:r+1]):
                stack.append(s[l:r+1])
                dfs(nextL, nextR)
                stack.pop()
            dfs(origL, origR + 1)

        dfs(0, 0)

        return res