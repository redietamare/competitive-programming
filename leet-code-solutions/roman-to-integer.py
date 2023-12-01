class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        summ=0
        for i in range(len(s)-1):
            if hashmap[s[i]]<hashmap[s[i+1]]:
                summ+=(-(hashmap[s[i]]))
            else:
                summ+=hashmap[s[i]]
        return summ +hashmap[s[-1]]