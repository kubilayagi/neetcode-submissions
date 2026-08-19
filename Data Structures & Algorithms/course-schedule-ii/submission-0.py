class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        res = []

        curpath = set()
        cleared = set()

        def dfs(crs):
            if crs in curpath:
                return False
            if crs in cleared:
                return True

            curpath.add(crs)
            for prq in adj[crs]:
                if not dfs(prq):
                    return False

            curpath.remove(crs)
            cleared.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res if len(res) == numCourses else []