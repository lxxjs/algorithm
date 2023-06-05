class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        for i in range(2,len(coordinates)):
            if (coordinates[i-1][0]-x0) * (coordinates[i][1]-coordinates[i-1][1]) != (coordinates[i-1][1]-y0) * (coordinates[i][0]-coordinates[i-1][0]):
                return False
        return True

# TIME COMPLEXITY : O(n)
# SPACE COMPLEXITY : O(1)