class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first={"q","w","e","r","t","y","u","i","o","p"}
        second={"a","s","d","f","g","h","j","k","l"}
        third={"z","x","c","v","b","n","m"}
        res = []
        for word in words:
            if word[0].lower() in first:
                place = first
            elif word[0].lower() in second:
                place = second
            else:
                place = third
            
            for i in range(len(word)):
                if word[i].lower() not in place:
                    break
            else:
                res.append(word)
        return res
                