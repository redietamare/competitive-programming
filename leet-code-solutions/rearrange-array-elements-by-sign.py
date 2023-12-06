class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        p = 0
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range(len(nums)//2):
            ans.append(pos[p])
            ans.append(neg[p])
            p+=1
        
        return ans