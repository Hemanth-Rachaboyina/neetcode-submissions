class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        for i in range(len(nums)-1):
            if new_nums[i] == new_nums[i+1]:
                return new_nums[i]
        