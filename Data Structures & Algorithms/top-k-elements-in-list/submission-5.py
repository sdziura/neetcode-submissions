class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = dict()
        freq = [[] for _ in nums]
        top = []
        
        for num in nums:
            occurences[num] = 1 + occurences.get(num, 0)

        for key, value in occurences.items():
            freq[value-1].append(key)
        
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                top.append(n)
                if len(top) == k:
                    return top
