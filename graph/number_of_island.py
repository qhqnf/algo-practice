class Solution:

    """
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        
        grid[i][j] = "0"
        
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid is None:
            return 0
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return

            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        if grid is None:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
