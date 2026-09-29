class Solution:

    def helper(self, height: List[int]):
        curr_h = 0
        curr_vol = 0
        all_vol = 0
        last_wall = 0
        for i, l in enumerate(height):
            if curr_h <= l:
                curr_h = l
                all_vol += curr_vol
                curr_vol = 0
                last_wall = i
            else:
                curr_vol += curr_h-l
        return all_vol, list(reversed(height[last_wall:]))

    def trap(self, height: List[int]) -> int:
        vol_1, new_height = self.helper(height)
        vol_2, _ = self.helper(new_height)
        return vol_1 + vol_2



        