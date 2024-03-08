class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hashmap = {}
        ans = []
        search = []
        for i in range(len(intervals)):
            search.append((intervals[i][0],i))
        search.sort()
        def checker(e):
            l=0
            r =len(intervals) -1
            cur = -1
            while l <=r:
                mid = (l+r)//2
                if search[mid][0]>=e:
                    r = mid-1
                    cur = search[mid][1]
                else:
                    l = mid + 1
            return cur
        for s,e in intervals:
            ans.append(checker(e))
        return ans



     
