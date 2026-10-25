class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict1 = defaultdict(int)
        for c in t:
            dict1[c] += 1
            n_unique = len(dict1)
        
        # sub = ""
        sub_i = -1
        sub_j = -1

        i = 0
        j = -1
        while i <= len(s) - len(t):            
            if s[i] not in dict1:
                i += 1
                continue
            else:
                j = max(i,j)
                while j < len(s) and n_unique > 0:
                    if s[j] in dict1:
                        dict1[s[j]] -= 1
                        if dict1[s[j]] == 0:
                            n_unique -= 1
                    j += 1
                if n_unique == 0:
                    if j - i  < sub_j - sub_i or sub_i == -1:
                        sub_i = i
                        sub_j = j
                        
                    
                dict1[s[i]] += 1
                if dict1[s[i]] == 1:
                            n_unique += 1
                i += 1
        return s[sub_i:sub_j]
