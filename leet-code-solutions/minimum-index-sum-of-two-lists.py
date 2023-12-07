class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1=defaultdict(int)
        for i in range(len(list1)):
            if list1[i] in list2:
                dic1[list1[i]]+=i
        for i in range(len(list2)):
            if list2[i] in dic1:
                dic1[list2[i]]+=i
        minn=min(list(dic1.values()))
        ans = []
        for i in dic1:
            if dic1[i]==minn:
                ans.append(i)
        return ans
            