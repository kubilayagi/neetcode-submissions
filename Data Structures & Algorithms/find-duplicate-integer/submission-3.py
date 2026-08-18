class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # note that num here is the actual number in the list itself
        # we are using a trick alotted to us by the constraints of the problem
        # specifically that 1 <= nums[i] <= n
        for num in nums:
            print(nums)
            if nums[abs(num)-1] < 0:
                return abs(num)
            else:
                nums[abs(num)-1] *= -1
        
        return -1