class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for i in range(2, n):
            x, y = coordinates[i]
            if (x - x0) * (y - y1) != (x - x1) * (y - y0) :
                return False
        return True

# TIME COMPLEXITY : O(n)
# SPACE COMPLEXITY : O(1)