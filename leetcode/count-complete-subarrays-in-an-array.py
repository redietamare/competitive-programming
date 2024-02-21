class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique=set(nums)
        count = l = 0
        check=defaultdict(int)
        for r in range(len(nums)):
            check[nums[r]] += 1
            while len(check) == len(unique):
                count += (len(nums) - r)
                check[nums[l]] -= 1
                if check[nums[l]] == 0:
                    del check[nums[l]]
                l += 1
        return count
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count=0
        # k=len(set(nums))
        # for i in range(len(nums)):
        #     seen=set()
        #     for j in range(i,len(nums)):
        #         seen.add(nums[j])
        #         if len(seen) == k:
        #             count += 1
        # return count