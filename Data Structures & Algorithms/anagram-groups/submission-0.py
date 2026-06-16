class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for w in strs:
            mp[''.join(sorted(w))].append(w)
        return list(mp.values())