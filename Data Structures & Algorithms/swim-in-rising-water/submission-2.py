class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # initally add 0, 0 to seen coords
        seen = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        ret = 0
        n = len(grid)
        
        while heap:

            maxHeight, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return maxHeight
            
            # checking up
            if r - 1 >= 0 and (r - 1, c) not in seen:
                heapq.heappush(heap, (max(maxHeight, grid[r - 1][c]), r - 1, c))
                seen.add((r - 1, c))

            # checking down
            if r + 1 < n and (r + 1, c) not in seen:
                heapq.heappush(heap, (max(maxHeight, grid[r + 1][c]), r + 1, c))
                seen.add((r + 1, c))

            # checking left
            if c - 1 >= 0 and (r, c - 1) not in seen:
                heapq.heappush(heap, (max(maxHeight, grid[r][c - 1]), r, c - 1))
                seen.add((r, c - 1))

            # checking right
            if c + 1 < n and (r, c + 1) not in seen:
                heapq.heappush(heap, (max(maxHeight, grid[r][c + 1]), r, c + 1))
                seen.add((r, c + 1))

        
        #    heapq.heapify(heap)

        return -1





