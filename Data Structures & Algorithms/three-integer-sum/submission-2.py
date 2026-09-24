class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        m = 1
        r = len(nums) - 1
        result = set()
        nums.sort()
        while m < r:
            while m < r:
                three_sum = nums[l] + nums[m] + nums[r]
                if three_sum == 0:
                    result.add((nums[l], nums[m], nums[r]))
                    r -= 1
                elif three_sum > 0:
                    r -= 1
                else:
                    m += 1
            l += 1
            m = l + 1
            r = len(nums) - 1
        return list(result)
            