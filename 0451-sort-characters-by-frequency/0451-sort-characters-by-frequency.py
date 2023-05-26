class Solution:
    def frequencySort(self, s: str) -> str:
        frequency=Counter(s)
        temp_array=[]
        ans=[]
        for key,value in frequency.items():
            temp_array.append((key,value))
        temp_array=sorted(temp_array ,key=lambda x:x[1],reverse=True)
        for i in temp_array:
            ans.extend([i[0]]*i[1])
        string="".join(ans)
        return string