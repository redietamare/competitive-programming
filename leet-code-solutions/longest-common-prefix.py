class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans=''
        minlen=min(len(strs[0]),len(strs[-1]))
        print(minlen)
        if minlen==0:return ans
        for i in range(minlen):
            if strs[0][i]==strs[-1][i]:
                ans+=strs[0][i]
            else:
                return ans
        return ans
        
        
        
        
        
        
        
        
        # res = ""
        # minlen=float("inf")
        # if len(strs)==1:
        #     return strs[0]
        # for i in strs:
        #     if len(i)<minlen:
        #         minlen=len(i)
        # for i in range(minlen):
        #     sett=set()
        #     for j in range(len(strs)):
        #         sett.add(strs[j][i])
        #     if len(sett)==1:
        #         res+=strs[j][i]
        #     else:
        #         return res
            
            
                
        

                
                
                