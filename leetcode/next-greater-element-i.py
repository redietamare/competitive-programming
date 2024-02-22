class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        ans = [-1]*len(nums1)
        #decreasing monotonic stack
        stack = []
       
        for i in range(len(nums1)):
            hashmap[nums1[i]] = i
        
        for num in nums2:
            while stack and stack[-1]<num:
                val = stack.pop()
                if val in hashmap:
                    ans[hashmap[val]] = num
            if not stack or stack[-1]>=num:
                stack.append(num)

        return ans