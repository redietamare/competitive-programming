class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        arr=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for i in range(len(pos)):
            arr.append(pos[i])
            arr.append(neg[i])
        return(arr)