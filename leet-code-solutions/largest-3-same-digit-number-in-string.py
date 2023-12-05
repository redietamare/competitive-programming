class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest=float("-inf")
        for i in range(len(num)-2):
            if len(set(num[i:i+3]))==1 and largest<int(num[i:i+3]):
                largest=int(num[i:i+3])
        if largest==float("-inf"):
            return ""
        if largest==0:
            return "000"
        else:
            return str(largest)