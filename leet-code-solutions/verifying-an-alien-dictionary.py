class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap=dict()
        for i in range(len(order)):
            hashmap[order[i]]=i
        # count=0
        # for i in range(len(words)-1):
        #     for j in range(min(len(words[i+1]),len(words[i]))):
        #         if (hashmap[words[i][j]]<hashmap[words[i+1][j]]):
        #             break
        #         elif (hashmap[words[i][j]]>hashmap[words[i+1][j]]):
        #             return False
        #     else:
        #         if (len(words[i])>len(words[i+1])):
        #             return False
        # return True
        for i in range(len(words)-1):
            if max(words[i],words[i+1], key=lambda x:[hashmap[chr] for chr in x])!=(words[i+1]):
                return False
        return True