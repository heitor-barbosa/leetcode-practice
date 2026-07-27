# First Solution, Incorrect Answer - forgot to consider edge cases ([0, 0, 1, 0, 1])
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 1 - Descobrir máximo de flores que podem ser colocadas
        #       1.1 - necessario 3 espacos vazios em sequencia para colocar uma flor
        # 2 - Comparar valor

        result = []
        count = 0
        new_flowers = 0

        for i in range (0, len(flowerbed)):
            if flowerbed[i] == 0:
                count += 1
            else:
                count = 0

            if count == 3:
                new_flowers += 1
                count = 1
        
        return n <= new_flowers
                

# Second solution, New way of defining max possible flower quantity    
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 1 - Descobrir máximo de flores que podem ser colocadas
        #       1.1 - necessario todos espacos adjacentes vazios (quando existir) para colocar uma flor
        # 2 - Comparar valor

        result = []
        count = 0
        new_flowers = 0

        # Algorithm for checking inner array
        for i in range (0, len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            if i == 0:
                if len(flowerbed) == 1:
                    new_flowers += 1
                if i + 1 < len(flowerbed) and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    new_flowers += 1     
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] == 0:
                    new_flowers += 1
            else:
                if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    new_flowers += 1
        
        return n <= new_flowers
                
