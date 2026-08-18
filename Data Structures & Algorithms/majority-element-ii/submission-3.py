class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, n2, n1count, n2count = 1000000001, 1000000001, 0, 0

        for i in range(len(nums)):
            if nums[i] == n1:
                n1count += 1
            elif nums[i] == n2:
                n2count += 1
            elif n1count == 0:
                n1 = nums[i]
                n1count = 1
            elif n2count == 0:
                n2 = nums[i]
                n2count = 1
            else:
                n1count -= 1
                n2count -= 1

        n1count = 0
        n2count = 0
        for k in nums:
            if k == n1:
                n1count += 1
            elif k == n2:
                n2count += 1

        res = []
        if n1count > (len(nums) / 3):
            res.append(n1)
        if n2count > (len(nums) / 3):
            res.append(n2)
        return res

