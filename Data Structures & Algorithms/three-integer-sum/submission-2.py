class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if nums[i] > 0:
                # short circuit, if we're in the positive numbers, we don't
                #   have negative numbers to get us to zero
                break
            if i > 0 and nums[i] == nums[i-1]:
                # to prevent duplicates on the i level loop
                continue
            j, k = (i+1), len(nums)-1
            while j < k:

                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j < k:
                        # to prevent duplicates on the j/k level loop
                        j+=1
                elif threeSum < 0:
                    j+=1
                else:
                    k-=1
        return res