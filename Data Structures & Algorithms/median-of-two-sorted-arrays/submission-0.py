class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        final = sorted(nums1)
        l = 0
        r = len(final)-1
        if len(final)%2 != 0:
            return final[(l+r)//2]
        else:
            m1 = (l+r)//2
            m2 = (l-r)//2
            median = (final[m1]+final[m2])/2

            return median

        
        