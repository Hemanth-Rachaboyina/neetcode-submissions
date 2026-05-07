class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-i for i in nums]

        maxheap = nums
        heapq.heapify(maxheap)

        while k>0:
            kth = heapq.heappop(maxheap)
            k-=1
        
        if kth > 0:
            return -kth
        if kth < 0:
            return abs(kth)
        if kth == 0:
            return 0
        
        