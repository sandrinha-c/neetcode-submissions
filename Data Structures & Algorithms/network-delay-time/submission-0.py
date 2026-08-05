class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        graph=[[]for _ in range (n+1)]
        dist=[float("inf")]*(n+1)
        dist[k]=0
        
        for item in times:
            source, target, cost=item
            graph[source].append((target, cost))

        heap=[(0,k)]
        while heap:
            curr_cost, target=heapq.heappop(heap)
            if curr_cost > dist[target]:
                continue
            dist[target]=curr_cost
            for neighbor, cost in graph[target]:
                new_cost=curr_cost+cost
                if new_cost<dist[neighbor]:
                    heapq.heappush(heap, (new_cost, neighbor))
                    dist[neighbor]=new_cost

        ans=max(dist[1:n+1])
        if ans==float("inf"):
            return -1
        else:
            return ans