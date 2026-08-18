class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy1 = nums1.copy()[:m]
        i = j = k = 0
        while k < n + m:
            if j >= n or (i < m and copy1[i] <= nums2[j]):
                nums1[k] = copy1[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1

        return
