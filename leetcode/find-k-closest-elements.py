class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # hashmap = defaultdict(list)
        # diff = []
        # for i in range(len(arr)) :
        #     dif = abs(arr[i]-x)
        #     diff.append(dif)
        #     hashmap[dif].append(i)
  
        # diff = set(diff)
        # diff = list(diff)
        # diff.sort()
        # ans = []
        # o=0
        # for i in diff:
        #     if len(hashmap[i])>1:
        #         for j in hashmap[i]:
        #             ans.append(arr[j])
        #             o += 1
        #             if o>=k:
        #                 return sorted(ans)
        #     else:
        #         ans.append( arr[hashmap[i][0]])
        #         o += 1
        #         if o>=k:
        #             return sorted(ans)
        l = 0
        r = len(arr) - 1
        while r - l>=k:
            if abs(arr[r]-x) >= abs(arr[l]-x):
                r -= 1
            else:
                l += 1
        ans = arr[l:r+1]
        return ans