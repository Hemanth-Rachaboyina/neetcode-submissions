class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm={}
        nums = numbers

        for i in range(len(nums)) :
            diff = target - numbers[i]

            if diff in hm:
                return [hm[diff], i + 1]

            hm[numbers[i]] = i + 1

        return []
        