class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxx = deque()
        minn = deque()
        l = 0
        length = 0
        for r in range(len(nums)):             
            while maxx and nums[r]>maxx[-1]:
                maxx.pop()
            maxx.append(nums[r])
            while minn and nums[r]<minn[-1]:
                minn.pop()
            minn.append(nums[r])
            while maxx and minn and abs(maxx[0] - minn[0]) > limit:
                if nums[l] == maxx[0]:
                    maxx.popleft()
                elif nums[l] == minn[0]:
                    minn.popleft()
                # print(minn,maxx,l,r)
                l+=1
            length = max(length,r-l+1)
            # print(minn,maxx)
        return length