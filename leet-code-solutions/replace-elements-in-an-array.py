class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashtable={}
        for i in range(len(nums)):
            hashtable[nums[i]]=i
        for i in range(len(operations)):
            hashtable[operations[i][1]]=hashtable[operations[i][0]]
            hashtable[operations[i][0]]=None

        for i in hashtable:
            if hashtable[i]!=None:
                nums[hashtable[i]]=i
        return(nums)