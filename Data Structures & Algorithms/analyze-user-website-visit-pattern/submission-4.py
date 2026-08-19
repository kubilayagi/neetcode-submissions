class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            visits[u].append(w)

        counts = collections.defaultdict(int)

        for u, w in visits.items():
            patterns = set()
            for i in range(0, len(w)):
                for j in range(i + 1, len(w)):
                    for k in range(j + 1, len(w)):
                        patterns.add((w[i], w[j], w[k]))

            for p in patterns:
                counts[p] += 1

        res = None
        count = -1
        for p, c in counts.items():
            if c > count or (c == count and p < res):
                res = p
                count = c

        return list(res)