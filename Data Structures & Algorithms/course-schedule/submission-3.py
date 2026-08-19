class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        path = set()
        cleared = set()
        def dfs(crs):
            if crs in path:
                return False
            if crs in cleared:
                return True
            path.add(crs)
            for prq in adj[crs]:
                if not dfs(prq):
                    return False

            path.remove(crs)
            cleared.add(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True