class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap={}
        for i in range(len(names)):
            hashmap[heights[i]]=names[i]
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                if heights[i]<heights[j]:
                    heights[i],heights[j]=heights[j],heights[i]
        ans=[hashmap[heights[i]] for i in range(len(heights))]
        return ans   
    