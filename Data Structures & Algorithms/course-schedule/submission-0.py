class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 建 graph
        # 2. 建 indegree
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append (course)
            indegree[course]+=1
        
        # 3. 把 indegree == 0 的課放進 queue
        from collections import deque
        queue=deque()
        for course, num_pre in enumerate(indegree) :
            if num_pre==0:
                queue.append (course)
        # 4. 不斷取出課程，更新鄰居的 indegree
        # 5. 計算 processed
        processed=0
        while queue:
            curr_course=queue.popleft()
            processed+=1
            for neighbor in graph [curr_course]:
                indegree[neighbor] -=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return processed == numCourses

# 6. 回傳 processed == numCourses
        