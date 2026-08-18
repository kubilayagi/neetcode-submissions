class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curtotal = numbers[l] + numbers[r]
            if curtotal == target:
                break
            elif curtotal < target:
                l+=1
            else:
                r-=1
        return [l+1, r+1]