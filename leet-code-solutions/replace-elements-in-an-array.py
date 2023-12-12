class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        
        for ops in operations:
            hashmap[ops[1]]=hashmap[ops[0]]
            del hashmap[ops[0]]
        
        for i in hashmap:
            if hashmap[i]!=None:
                nums[hashmap[i]]=i
        return nums
    
    
    
    
    
    
    
    
        
        
        
        
        
        
#         hashtable={}
#         for i in range(len(nums)):
#             hashtable[nums[i]]=i
#         print(hashtable)
#         for i in range(len(operations)):
#             hashtable[operations[i][1]]=hashtable[operations[i][0]]
#             hashtable[operations[i][0]]=None
#             print(hashtable)
        

#         for i in hashtable:
#             if hashtable[i]!=None:
#                 nums[hashtable[i]]=i
#         return(nums)