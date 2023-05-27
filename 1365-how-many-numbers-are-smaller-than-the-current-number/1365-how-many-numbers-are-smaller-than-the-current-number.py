class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        x=Counter(nums)
        keys=list(x.keys())
        keys.sort()
        start=0
        for i in range(len(keys)):
            dic[keys[i]]=start
            start+=x[keys[i]]
        for i in range(len(nums)):
            nums[i]=dic[nums[i]]
        print(dic)
        return(nums)

