class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {i:0 for i in range(1,n+1)}
        trustedby = {i:0 for i in range(1,n+1)}
        judge = -1
        judgecount = 0

        for a, b in trust:
            trusts[a] += 1
            trustedby[b] += 1

        print(trusts)
        print(trustedby)

        for p, t in trusts.items():
            if t == 0 and trustedby[p] == (n - 1):
                judgecount += 1
                judge = p

        return judge if judgecount < 2 else -1