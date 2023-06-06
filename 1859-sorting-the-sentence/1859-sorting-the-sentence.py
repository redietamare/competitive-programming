class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        sentence=[]
        for i in s:
            s.sort(key=lambda x:x[-1])
        for i in s:
            x=i[0:-1]
            sentence.append(x)
            e=" ".join(sentence)
        return e
