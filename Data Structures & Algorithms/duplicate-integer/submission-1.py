class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # s_nums = set(nums)

        if len(nums) == len(set(nums)):
            return False
        return True
        