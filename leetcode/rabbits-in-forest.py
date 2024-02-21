class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # hashmap = Counter(answers)
        # # print(hashmap)
        # ans = 0
        # for i in hashmap:
        #     if i != 0:
        #         # print(ceil(hashmap[i]/(i+1))*(i+1),"here")
        #         ans += (ceil(hashmap[i]/(i+1))*(i+1))  
        # ans += hashmap[0]
        # return ans
        
        count = {}
      
        for val in answers:
            if val in count:
                count[val] -= 1
            else:
                count[val] = val
            if count[val] == 0:
                count.pop(val)
            
        ans = len(answers)
        
        for val in count.values():
            ans += val
        return ans
        
# [1,1,1]
# [0,0,1,1,1] 
# [1,1,1,1]
# [1,1,1,1,1]
# [1,0,1,0,0]
# [3,3,1,2,3]
# [10,10,10]