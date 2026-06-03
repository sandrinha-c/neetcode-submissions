class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_wd={}

        for word in strs:
            arr_wd_cnt=[0]*26 # reset count for each word!
            for ch in word:
                arr_wd_cnt[ord(ch)-ord('a')]+=1
            key=tuple(arr_wd_cnt)
            if key not in dict_wd:
                dict_wd[key]=[word] #wrap in a list
            else:
                dict_wd[key].append(word)
        return (list(dict_wd.values()))