class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        
        def checker(cap):
            i = 0
            summ =0
            day = 0
            while i <len(weights):
                if summ + weights[i] <= cap:
                    summ += weights[i]
                    i += 1
                else:
                    day += 1
                    summ = 0 
                
            return day + 1
        l = max(weights)
        h = sum(weights)
        def helper(l,h):
            l -= 1
            h+=1
            while l+1<h:
                mid = (l+h)//2
                print(l,h,mid,checker(mid))
                if checker(mid)<=days:
                    h = mid
                else:
                    l = mid
            return l+1
        return helper(l,h)





