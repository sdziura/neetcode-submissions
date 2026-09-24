class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        m = 1
        r = len(nums) - 1
        result = []
        nums.sort()
        while m < r:
            while m < r:
                three_sum = nums[l] + nums[m] + nums[r]
                if three_sum == 0:
                    result.append([nums[l], nums[m], nums[r]])
                    r -= 1
                    while m < r and nums[r] == nums[r+1]:
                        r -= 1      
                elif three_sum > 0:
                    r -= 1
                else:
                    m += 1
            i = l + 1
            while nums[l] == nums[i] and i<len(nums)-2:
                i += 1
            l = i
            m = l + 1
            r = len(nums) - 1
        return result
            