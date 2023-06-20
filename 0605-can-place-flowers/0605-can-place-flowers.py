class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        Yes=0
        flowerbed.append(0)
        if flowerbed[0]==0:
            if flowerbed[1]==0:
                flowerbed[0]=1
                Yes+=1
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    Yes+=1
        if Yes>=n:
            return True
        else:
            return False
    
                