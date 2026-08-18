class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        mp = collections.defaultdict(list)
        for (time, user, site) in sorted(zip(timestamp, username, website)):
            mp[user].append(site)

        counts = collections.defaultdict(int)
        
        for user in mp:
            patterns = set()
            cur = mp[user]
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    for k in range(j + 1, len(cur)):
                        patterns.add((cur[i], cur[j], cur[k]))

            for p in patterns:
                counts[p] += 1
        
        maxcount = 0
        res = tuple()

        for pattern in counts:
            if counts[pattern] > maxcount or (counts[pattern] == maxcount and pattern < res):
                maxcount = counts[pattern]
                res = pattern


        return list(res)

        