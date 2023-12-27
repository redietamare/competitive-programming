class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        setn1=set(nums1)
        setn2=set(nums2)
        hash1=Counter(nums1)
        for i in nums2:
            if i in hash1:
                ans.append(i)
                hash1[i]-=1
                if hash1[i]==0:
                    del hash1[i]
        return ans
                
        