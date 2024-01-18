class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+2)
        ans = []
        for book in bookings:
            st = book[0]
            ep = book[1]
            seat = book[2]
            prefix[st] += seat
            prefix[ep+1] -= seat
            # print(prefix)
        num = 0
        for i in prefix:
            num+=i
            ans.append(num)
        # return prefix
        return ans[1:len(ans)-1]
            