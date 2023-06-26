class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per=list(permutations(nums))
        for i in range(len(per)):
            per[i]=list(per[i])
        return(per)
                
        
        