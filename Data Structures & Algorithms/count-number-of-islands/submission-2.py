class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island=0
        seen=set()

        def canVisit(pos):
            r,c=pos
            if r not in range (len(grid)) or c not in range (len(grid[0])):
                return False
            if (r,c) in seen:
                return False
            if grid[r][c] == "0":
                return False
            return True
        
        def explore(pos):
            r,c=pos
            neighbors=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            seen.add(pos)
            for neighbor in neighbors:
                if canVisit(neighbor):
                    explore(neighbor)
                

        for r in range (len(grid)):
            for c in range(len(grid[0])):
                pos=(r,c)
                if canVisit(pos):
                    island+=1
                    explore(pos)
        return island

