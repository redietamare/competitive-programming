class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        buckets,ans = [], []
        if len(digits) == 0:
            return []
        def letter(i):
            if len(digits) == len(buckets):
                ans.append("".join(buckets))
            for j in range(i,len(digits)):
                d = hashmap[int(digits[j])]
                for k in range(len(d)):
                    buckets.append(d[k])
                    letter(j+1)
                    buckets.pop()
        letter(0)
        return ans




        return ["a"]