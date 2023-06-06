class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        maxx=max(nums)
        count=[0]*(maxx+1)
        listt=[]
        for i in range(len(nums)):
            count[nums[i]]+=1
        for i in range(len(count)):
            x=[i]*count[i]
            listt.extend(x)
        hashmap=defaultdict(list)
        for i in range(len(listt)):
            hashmap[listt[i]].append(i)
        return (hashmap[target])