class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        hashh={}
        sor=sorted(nums)
        for i in range(len(sor)):
            if sor[i] not in hashh:
                hashh[sor[i]]=i
        for i in range(len(nums)):
            ans.append(hashh[nums[i]])
        return ans