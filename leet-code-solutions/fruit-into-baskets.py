class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        max_fruits = 1
        trees = defaultdict(int)
        for r in range(len(fruits)):
            trees[fruits[r]]+=1
            while len(trees)>2:
                trees[fruits[l]] -= 1
                if trees[fruits[l]] == 0:
                    del trees[fruits[l]]
                l+=1
            max_fruits = max(max_fruits,r-l+1)
    
        return max_fruits
            