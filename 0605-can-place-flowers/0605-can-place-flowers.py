class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Initiate a couner for new flowers 
        new_flower_count = 0
        # Ensure that there are three 0's in a row to plant a flower in the middle + starting + ending case  
        for i in range(1,len(flowerbed)-1):
            # Starting case
            if i == 1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                flowerbed[i-1] = 1
                new_flower_count += 1 
                
            # Middle case
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                new_flower_count += 1  
                
            # Ending case
            if i == len(flowerbed)-2 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i+1] = 1
                new_flower_count += 1 
                
        # Checking case where there are only one/two place in the flowerbed
        if len(flowerbed) <= 2 and not 1 in flowerbed:
            new_flower_count += 1
        if new_flower_count >= n:
            return True 
        else:
            return False
        