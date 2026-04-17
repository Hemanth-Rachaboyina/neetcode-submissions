class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k-1
        final = []


        while r < len(nums):
            new = nums[l:r+1]
            final.append(max(new))
            l = l+1 
            r = r+1
        
        return final
        