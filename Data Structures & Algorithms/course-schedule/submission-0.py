class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for crs, prq in prerequisites:
            dep[crs].append(prq)

        finished = set()

        def dfs(crs):
            if crs in finished:
                return False
            if not dep[crs]:
                return True
            finished.add(crs)
            for prq in dep[crs]:
                if not dfs(prq):
                    return False
            finished.remove(crs)
            dep[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

        


    def weirdAnswer(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for crs, prq in prerequisites:
            dep[crs].append(prq)
            indegree[prq] += 1 # count how many classes have dependence on this class

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finished = 0
        while q:
            crs = q.popleft()
            finished += 1
            for prq in dep[crs]:
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    q.append(prq)
        
        return finished == numCourses