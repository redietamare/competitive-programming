class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxarea=0
        while left<=right:
            minn=(min(height[left],height[right]))
            currentarea=minn*(right-left)
            maxarea=max(maxarea,currentarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea