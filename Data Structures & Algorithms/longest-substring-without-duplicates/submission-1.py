class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        seen=set()
        l=0
        for ss in s:
            while ss in seen:
                seen.remove(s[l])
                l+=1
            seen.add(ss)
            curr_len=len(seen)
            max_len=max(curr_len, max_len)
        return max_len
