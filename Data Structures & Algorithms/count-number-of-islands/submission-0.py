class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island=0
        seen=set()
        rows= len (grid)
        cols= len (grid[0])

        def can_visit(pos):
            r,c=pos
            if r >= rows or r<0 or c>=cols or c<0:
                return False
            if pos in seen:
                return False
            if grid[r][c] != "1":
                return False
            return True

        def explore(pos):
            r,c=pos
            seen.add(pos)
            neighbors=[(r-1,c),(r+1,c),(r, c-1), (r,c+1)]
            for neighbor in neighbors:
                if can_visit(neighbor):
                   
                    explore(neighbor)

        for r in range (rows):
            for c in range(cols):
                if can_visit((r,c)):
                    island+=1
                    explore((r,c))
        return island 