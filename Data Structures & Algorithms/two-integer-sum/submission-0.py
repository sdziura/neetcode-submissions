class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = dict()
        for i, n in enumerate(nums):
            if (target - n) in checked:
                return [checked[target - n], i]
            else:
                checked[n] = i
