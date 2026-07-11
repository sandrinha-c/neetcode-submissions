class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps={}
        ans=[]
        for num in nums:
            maps[num]=maps.get(num,0)+1
        items=list(maps.items())
        items.sort(key=lambda pair:  pair[1],reverse=True )
            
        for _ in range (k):
            ans.append(items[_][0])
        return ans