class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        max_height = max(heights)
        top_volume = 0
        
        left = 0
        right = length - 1
        while left < right:
            volume = 0
            width = right - left
            if heights[left] > heights[right]:
                volume = heights[right] * width
                right -= 1
            else:
                volume = heights[left] * width
                left += 1
            if top_volume < volume:
                top_volume = volume
        return top_volume
