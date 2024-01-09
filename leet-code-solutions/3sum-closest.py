class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        ans = 0
        for i in range(len(nums)-1):
            l = i+1
            r = len(nums)-1
            while l<r:
                summ = nums[i]+nums[l]+nums[r]
                if summ==target:
                    return summ
                elif abs(summ-target)<diff:
                    diff=abs(summ-target)
                    ans = summ
                if summ>target:
                    r-=1
                else:
                    l+=1
        return ans