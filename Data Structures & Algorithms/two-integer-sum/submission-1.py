class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            num_we_need = target - n
            if num_we_need in hm:
                return [hm[num_we_need], i]
            hm[n] = i
        