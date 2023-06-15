class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1=0
        p2=0
        merged=[]
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]>nums2[p2]:
                merged.append(nums2[p2])
                p2+=1
            else:
                merged.append(nums1[p1])
                p1+=1
        merged.extend(nums1[p1:])
        merged.extend(nums2[p2:])
        n=len(merged)
        med=int(n/2)
        if n%2==0:
            median=(merged[med-1] + merged[med])/2
        else:
            median=merged[floor(med)]
        return(median)
        