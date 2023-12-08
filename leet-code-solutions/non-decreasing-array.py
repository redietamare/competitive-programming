class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)-1):
            if i!=0:
                if nums[i+1] < nums[i]:
                    if nums[i-1]<=nums[i+1]:
                        nums[i] = nums[i-1]
                        count +=1
                    else:
                        nums[i+1]=nums[i]
                        count += 1
                    if count > 1:
                        return False
            else:
                if nums[i+1] < nums[i]:
                    count += 1
        return True                