class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one, two = m-1, n-1
        last = m + n - 1
        
        while last >= 0:
            if one < 0:
                nums1[last] = nums2[two]
                two-=1
            elif two < 0:
                one-=1
            elif nums1[one] >= nums2[two]:
                nums1[last] = nums1[one]
                one-=1
            elif nums1[one] < nums2[two]:
                nums1[last] = nums2[two]
                two-=1
            last-=1

        return
            