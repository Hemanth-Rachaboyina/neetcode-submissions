class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        index_2 = None 

        for i in range(len(nums)):
            
            diff = target - nums[i]
            index_1 = i
            for key, value in hm.items():
                if value == diff:
                    index_2 = key
            
            hm[i] = nums[i]
            if index_1 is not None and index_2 is not None :
                return sorted([index_1, index_2])




        