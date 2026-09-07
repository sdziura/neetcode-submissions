class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            seen = {nums.pop(0)}
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False