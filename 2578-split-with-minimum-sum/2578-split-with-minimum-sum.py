class Solution:
    def splitNum(self, num: int) -> int:
        nums=list(str(num))
        nums.sort()
        str1=""
        str2=""
        for i in range(0,len(nums),2):
            str1+=nums[i]
        for i in range(1,len(nums),2):
            str2+=nums[i]
        return(int(str1)+int(str2))
        
        
        
        