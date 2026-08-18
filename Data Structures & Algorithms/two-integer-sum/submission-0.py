class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i in range(0, len(nums)):
            idx = target - nums[i]
            if idx not in needs:
                needs[idx] = i
        print(needs)
        for j in range(0, len(nums)):
            if nums[j] in needs and j != needs[nums[j]]:
                foundidx = needs[nums[j]]
                return [min(j, foundidx), max(j, foundidx)]
        return[-1,-1]