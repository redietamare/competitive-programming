class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evensum=0
        arr=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                evensum+=nums[i]
        for ques in queries:
            if (nums[ques[1]] + ques[0])%2==0:
                if nums[ques[1]]%2==0:
                    evensum+=ques[0]
                else:
                    evensum+=(nums[ques[1]] + ques[0])
            else:
                if(nums[ques[1]])%2==0:
                    evensum-=nums[ques[1]]
            nums[ques[1]]+=ques[0]
            arr.append(evensum)
        return arr
                