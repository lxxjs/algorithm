class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        plantable = 1
        from math import floor
        for i in range(len(flowerbed)):
            if counter >= n:
                return True
            if flowerbed[i] == 0:
                plantable += 1
            elif flowerbed[i] == 1:
                if plantable > 2:
                    counter += floor((plantable - 1) / 2) 
                plantable = 0
        if plantable >= 2:
            counter += floor(plantable / 2)
        if counter >= n:
            return True
        return False