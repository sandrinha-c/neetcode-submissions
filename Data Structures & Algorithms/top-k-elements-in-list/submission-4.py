class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps={}
        for num in nums:
            maps[num]=maps.get(num,0)+1
        items=list(maps.items())
        items.sort(key=lambda pair:  pair[1],reverse=True )
        print (items)
        ans=[]
        for num, freq in items:
            ans.append(num)
            if len(ans)==k:
                return ans
            