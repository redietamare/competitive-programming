class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        maxx=0
        visted=dict()
        for num in nums:
            if num in visted: continue
            i=1
            while num+i in sett:
                if (num+i in visted):
                    visted[num]=i+visted[num+i]
                    break
                else:
                    visted[num+i]=-1
                    i+=1
            else:
                visted[num]=i
            maxx=max(maxx,visted[num])
        return maxx
                    
                    