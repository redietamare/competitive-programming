class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return False
        i=0
        flag = False
        if nums[1]>nums[0]:
            while i < len(nums) -1:
                if nums[i]!=nums[i+1]:
                    while i <len(nums)-1 and nums[i+1]<nums[i]:
                        flag = True
                        i+=1
                else:
                    return False
                if flag == True and i == len(nums)-1:
                    return True
                elif flag == True :
                    return False
                else:
                    i+=1
            return False
        else: return False
            
        # i=0
        # while i < len(nums)-1:
        #     if nums[i+1]>nums[i]:
        #         while i <len(nums)-1 and nums[i+1]>nums[i]:
        #             i+=1
        #         if nums[i]!=nums[i+1]:
        #             while i< len(nums)-1 and nums[i+1]<nums[i]:
        #                 i+=1
        #         if i+1!=len(nums):
        #                 return False
        #         else:
        #             return False
        #     else: return False
        # return True
            