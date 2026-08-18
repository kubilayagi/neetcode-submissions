class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(l, r) -> List[int]:
            i, j = 0, 0
            res = []
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1

            if i == len(l):
                return res + r[j:]
            elif j == len(r):
                return res + l[i:]

            return res

        def sort(n):
            if not n or len(n) == 1:
                return n
            mid = len(n) // 2
            return merge(sort(n[:mid]), sort(n[mid:]))

        return sort(nums)

            