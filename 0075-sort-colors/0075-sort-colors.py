class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxx=max(nums)
        count=[0]*(maxx+1)
        c=1
        for i in range(len(nums)):
            count[nums[i]]+=c
        listt=[]
        for i in range(len(count)):
            x=[i]*count[i]
            listt.extend(x)
        for i in range(len(nums)):
            nums[i]=listt[i]


        

