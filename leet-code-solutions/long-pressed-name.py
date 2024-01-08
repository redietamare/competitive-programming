class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1=p2=0
        length=0
        lenn =1
        for i in range(len(name)-1):
            if name[i+1]!=name[i]:
                lenn+=1
        while p1<len(name) and p2<len(typed):
            length+=1
            l1 = 1
            l2 = 1
            if name[p1]==typed[p2]:
                while p1+1 < len(name) and name[p1 + 1] == name[p1]:
                    p1+=1
                    l1 += 1
                while p2 + 1< len(typed) and typed[p2+1] == typed[p2]:
                    p2 += 1
                    l2+=1
                # print(l1,l2)
                if l2<l1:
                    return False
            else:
                return False
            p1+=1
            p2+=1
        # print(length,lenn)
        if lenn>length:
            return False
        # print(name[-1],typed[-1])
        # print(p1,p2)
        if name[-1]!=typed[-1] or p2-1!=len(typed)-1:
            return False
        return True