class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=Counter(nums)
        good=0
        for i in count:
            good+=count[i]*(count[i]-1)//2
        return good
            
        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        # return count
        return 5