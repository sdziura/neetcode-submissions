class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_char = defaultdict(int)
        l = 0
        res = 0
        for r, ch in enumerate(s):
            count_char[ch] += 1

            while (r - l + 1) - max(count_char.values()) > k:
                count_char[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res

            
