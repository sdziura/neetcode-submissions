class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictA = {}
        for letter in s:
            if letter in dictA:
                dictA[letter] += 1
            else:
                dictA[letter] = 1
        
        for letter in t:
            if letter not in dictA:
                return False
            dictA[letter] -= 1
        
        for count in dictA.values():
            if count != 0:
                return False
        
        return True