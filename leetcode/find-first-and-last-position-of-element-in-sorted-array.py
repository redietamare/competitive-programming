class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # l = -1
        # r =  len(nums)
        # ans=[-1,-1]
        if target not in nums:
            return [-1,-1]
        # while l + 1 < r:
        #     mid = (l+r)//2
        #     if nums[mid]>=target:
        #         r = mid
        #     else:
        #         l = mid
        # ans[0] = r
        # l = -1
        # r =  len(nums)
        # while l + 1 < r:
        #     mid = (l+r)//2
        #     if nums[mid]<=target:
        #         l = mid
        #     else:
        #         r = mid
        # ans[1] = l

        # return ans

        f = (bisect_left(nums,target))
        s = (bisect_right(nums,target))
        return [f,s-1]
