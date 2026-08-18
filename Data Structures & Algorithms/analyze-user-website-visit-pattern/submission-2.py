class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        adj = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            adj[u].append(w)

        counts = collections.defaultdict(int)
        for u, w in adj.items():
            patterns = set()
            for i in range(len(w)):
                for j in range(i + 1, len(w)):
                    for k in range(j + 1, len(w)):
                        patterns.add((w[i], w[j], w[k]))

            for p in patterns:
                counts[p] += 1


        maxcount = 0
        res = tuple()

        for p, c in counts.items():
            if c > maxcount or (c == maxcount and p < res):
                res = (p)
                maxcount = c

        return list(res)

