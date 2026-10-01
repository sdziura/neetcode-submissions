class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        checked = set()
        i = 0
        start = 0
        max_len = 0
        while i < len(s):
            if s[i] in checked:
                max_len = max(i-start, max_len)
                while s[start] != s[i]:
                    checked.remove(s[start])
                    start += 1
                checked.remove(s[start])
                start += 1
            else:
                checked.add(s[i])
                i += 1

        return max(i-start, max_len)