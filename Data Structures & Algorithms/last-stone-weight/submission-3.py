import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
            
        while len(heap)>1:
            y,x=-heapq.heappop(heap), -heapq.heappop(heap)
            if y-x !=0:
                heapq.heappush(heap,-(y-x))
         
        if heap:
            return -heap[0]
        else:
            return 0
            


        