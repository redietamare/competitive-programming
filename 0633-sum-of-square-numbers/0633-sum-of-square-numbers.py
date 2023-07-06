class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrtc=ceil(sqrt(c))
        left=0
        right=sqrtc
        listt=list(range(0,sqrtc+1))
        while right>=left:
            num=((listt[left])**2 + (listt[right])**2)
            if num==c:
                return True
            if num>c:
                right-=1
            else:
                left+=1
        return False