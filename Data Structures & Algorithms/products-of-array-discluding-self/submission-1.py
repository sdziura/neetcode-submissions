class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =  len(nums)
        prefix_mult = [1] * n
        temp = 1
        for i in range(n):
            prefix_mult[i] = temp
            temp *= nums[i]

        temp = 1
        for j in range(n - 1, -1, -1):
            prefix_mult[j] *= temp
            temp *= nums[j]

        return prefix_mult
