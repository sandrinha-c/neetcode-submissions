class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps={}
        for word in strs:
            key=''.join(sorted(word))
            if key in maps:
                maps[key].append(word)
            else:
                maps[key]=[]
                maps[key].append(word)
        return list(maps.values())
