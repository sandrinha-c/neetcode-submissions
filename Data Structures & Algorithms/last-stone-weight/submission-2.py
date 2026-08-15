import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
            
        while len(heap)>1:
            heapq.heapify(heap)
            print (heap)
            y,x=-heap[0], -heap[1]
            if x==y:
                heapq.heappop(heap)
                heapq.heappop(heap)
            elif x <y:
                y,x=-heapq.heappop(heap), -heapq.heappop(heap)
                heapq.heappush(heap,-(y-x))
               
         
        if heap:
            return -heap[0]
        else:
            return 0
            


        