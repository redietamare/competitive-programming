class Solution:
    def minProcessingTime(self, pt: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        pt.sort()
        maxx=0
        pt1=-1
        for i in range(len(tasks)):
            if i%4==0:
                pt1+=1
            summ=pt[pt1]+tasks[i]
            maxx=max(maxx,summ)
        return maxx
            