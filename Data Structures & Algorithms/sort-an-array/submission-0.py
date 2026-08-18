class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return nums
        split = len(nums) // 2
        left, right = self.sortArray(nums[0:split]), self.sortArray(nums[split:])
        res = []
        i, j = 0, 0
        while len(res) < (len(left) + len(right)):
            if i == len(left):
                res = res + right[j:]
                break
            elif j == len(right):
                res = res + left[i:]
                break
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        return res