class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for k, v in counts.items():
            if v > len(nums) // 2:
                return k
        return -1
