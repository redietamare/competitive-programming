class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        summ=0
        left,right=0,len(people)-1
        while right>=left:
            cursum=people[left]+people[right]
            if cursum<=limit:
                left+=1
                right-=1
            else:
                right-=1
            summ+=1
        return summ