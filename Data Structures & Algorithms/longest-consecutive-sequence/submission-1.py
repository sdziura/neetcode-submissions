class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        top_length = 0
        while nums_set:
            current_length = 1
            current = nums_set.pop()
            
            post = current + 1
            while post in nums_set:
                nums_set.discard(post)
                current_length += 1
                post += 1

            pre = current - 1
            while pre in nums_set:
                nums_set.discard(pre)
                current_length += 1
                pre -= 1

            if current_length > top_length:
                top_length = current_length

        return top_length