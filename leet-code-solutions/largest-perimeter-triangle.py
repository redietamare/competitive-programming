class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxper = 0
        nums.sort()
        for i in range(len(nums)-3+1):
            a,b,c = nums[i:i+3]
            print(a,b,c)
            if ((a + b)>c) and ((b+c)>a) and ((a+c)>b):
                maxper=a+b+c
        return maxper