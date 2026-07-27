class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for x, y in points:
            dist=x**2+y**2
            heapq.heappush(heap, (-dist,(x,y)))
            if len(heap)>k:
                heapq.heappop(heap)
        for freq, location in heap:
            ans.append(location)
        return ans
