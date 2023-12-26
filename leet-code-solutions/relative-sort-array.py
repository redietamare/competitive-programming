class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        notinarr=[]
        hashmap={}
        ans=[]
        for i in range(len(arr2)):
            hashmap[arr2[i]] = 0
        for i in range(len(arr1)):
            if arr1[i] not in hashmap:
                notinarr.append(arr1[i])
            else:
                hashmap[arr1[i]]+=1
        for i in range(len(arr2)):
            ans.extend([arr2[i]]*hashmap[arr2[i]])
        notinarr.sort()
        ans.extend(notinarr)
        return ans