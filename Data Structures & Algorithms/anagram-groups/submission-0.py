class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for s in strs:
            m = ''.join(sorted(s))
            data[m].append(s)
        return list(data.values())



        