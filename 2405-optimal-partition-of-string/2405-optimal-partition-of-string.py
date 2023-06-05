class Solution:
    def partitionString(self, s: str) -> int:
        currentset=set()
        minnum=1
        for i in s:
            if i in currentset:
                minnum+=1
                currentset=set()
            currentset.add(i)
        return(minnum)

