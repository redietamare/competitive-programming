class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in paths:
            arr=i.split()
            for j in range(1,len(arr)):
                s=arr[j].split("(")
                dic[s[1]].append(arr[0]+"/"+s[0])
        ans=[dic[i] for i in dic if len(dic[i])>1]
        return ans