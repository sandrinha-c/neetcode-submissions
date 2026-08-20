class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        seen=set()
        len_r=len(grid)
        len_c=len(grid[0])
        def canVisit(r,c):
            if r not in range (len_r) or c not in range (len_c):
                return False
            if (r,c) in seen:
                return False
            if grid[r][c]==0:
                return False
            return True
        def explore (r,c):
            area=0
            if canVisit(r,c):
                area+=1
                seen.add((r,c))
                neighbors=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
                for nr,nc in neighbors:
                    area+=explore(nr,nc)
            return area
        for r in range (len_r):
            for c in range (len_c):
                if canVisit(r,c):
                    area=explore(r,c)
                    max_area=max(area,max_area)
        return max_area