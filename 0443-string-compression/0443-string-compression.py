class Solution:
    def compress(self, chars: List[str]) -> int:
        s=[]
        left=0
        right=1
        summ=0
        while right<len(chars):
            if chars[left]==chars[right]:
                right+=1
            else:
                freq=right-left
                s.append(chars[left])
                if freq!=1:
                    s.extend(list(str(freq)))
                left+=freq
                right+=1
        freq=right-left
        s.append(chars[left])
        if freq!=1:
            s.extend(list(str(freq)))
        chars[::]=s[::]
        
        return(len(chars))

        