class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1] * N
        suffix = [1] * N

        prefix[0] = nums[0]
        for i in range(1, N):
            prefix[i] = prefix[i-1] * nums[i]

        suffix[N-1] = nums[N-1]
        for j in range(N-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j]

        res = []

        for k in range(N):
            left = 1
            right = 1
            if k > 0:
                left = prefix[k-1]
            if k < (N - 1):
                right = suffix[k+1]
            res.append(left * right)

        return res