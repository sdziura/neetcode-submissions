class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = []
        temp = 1
        for n in nums:
            prefix_mult.append(temp)
            temp *= n

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix_mult[i] *= temp
            temp *= nums[i]

        return prefix_mult
