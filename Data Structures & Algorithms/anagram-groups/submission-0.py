class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            alphabet = [0] * 26
            for w in word:
                alphabet[ord(w) - ord("a")] += 1
            groups[tuple(alphabet)].append(word)

        return list(groups.values())
