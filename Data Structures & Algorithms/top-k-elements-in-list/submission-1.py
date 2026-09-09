class Solution:
    def sortFromMin(self, e):
        return e[1]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = dict()
        top = list()
        
        for num in nums:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1
        
        for (key, value) in occurences.items():
            if len(top) < k:
                top.append((key, value))
                top.sort(key=self.sortFromMin)
            else:
                if value > top[0][1]:
                    top[0] = (key, value)
                    top.sort(key=self.sortFromMin)
        return [t[0] for t in top]
                


