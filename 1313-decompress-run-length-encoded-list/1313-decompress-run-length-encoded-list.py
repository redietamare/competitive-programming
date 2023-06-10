class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(0,len(nums),2):
            value=[nums[i+1]]*nums[i]
            arr.extend(value)
        return(arr)
            
            
        