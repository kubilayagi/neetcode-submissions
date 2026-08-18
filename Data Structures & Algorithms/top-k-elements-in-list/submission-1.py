class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freqs = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, count in counts.items():
            freqs[count].append(num)
        stillneed = k
        for i in range(len(freqs)-1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []