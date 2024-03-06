class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while l + 1<r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid 
            elif nums[mid] > target:
                r = mid 
        return -1
        # l = 0
        # h= len(nums) - 1 
        # while l<=h:
        #     mid = (l + h)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         h = mid - 1
        #     print(mid,l,h)
        # return -1
