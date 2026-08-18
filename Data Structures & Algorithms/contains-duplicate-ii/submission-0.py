class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = {}
        for i in range(len(nums)):
            if nums[i] in s:
                for j in s[nums[i]]:
                    if abs(i - j) <= k:
                        return True
                s[nums[i]].append(i)
            else:
                s[nums[i]] = [i]

        return False