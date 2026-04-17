class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sor = sorted(set(nums))
        n = len(sor)

        longest = 1
        current = 1

        for i in range(n - 1):
            if sor[i + 1] - sor[i] == 1:
                current += 1
            else:
                current = 1   # 🔥 THIS WAS MISSING

            longest = max(current, longest)

        return longest