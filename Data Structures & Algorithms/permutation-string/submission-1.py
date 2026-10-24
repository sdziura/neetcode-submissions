class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1_main = defaultdict(int)
        for c in s1:
            dict1_main[c] += 1
        dict1_copy = dict1_main.copy()
        
        for i in range(len(s2)):
            if len(s2)-i < len(s1):
                return False
                
            if dict1_main[s2[i]] > 0:
                dict1_copy = dict1_main.copy()
                sub_s2 = s2[i:i+len(s1)]
                win = True
                for cc in sub_s2:
                    if dict1_copy[cc] > 0:
                                dict1_copy[cc] -= 1
                    else:
                        win = False
                        break	
                if win:
                    return True
        return False