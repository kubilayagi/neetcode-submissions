class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o, c, cur):
            if o > n or c > n or c > o:
                return
            if len(cur) == 2 * n:
                res.append(cur)
                return
            
            cur = cur + "("
            dfs(o + 1, c, cur)
            cur = cur[:-1]
            if o > c:
                cur = cur + ")"
                dfs(o, c + 1, cur)
                cur = cur[:-1]

            return

        dfs(0, 0, "")
        return res

            
