class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        j = n - 1
        for i in range(m):
            while j > -1:
                if grid[i][j] < 0:
                    count += m - i
                    j -= 1
                else:
                    break
        return count