class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = {5:0,10:0,20:0}
        for i in bills:
            hashmap[i]+=1
            if i == 10:
                if not hashmap[5]:
                    return False
                else:
                    hashmap[5]-=1
            elif i == 20:
                if (not hashmap[10] and hashmap[5]<3) or (hashmap[10] and not hashmap[5]):  
                    return False
                elif hashmap[10] and hashmap[5]:
                    hashmap[5] -= 1
                    hashmap[10] -= 1
                elif not hashmap[10] and hashmap[5]>=3:
                    hashmap[5]-=3
                  
            # print(hashmap)
        return True