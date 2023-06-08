class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m-1, -1, -1):
            if grid[i][n-1] < 0:
                count += 1
                for j in range(n-2,-1,-1):
                    if grid[i][j] >= 0:
                        break
                    else:
                        count += 1
            else:
                break

        return count