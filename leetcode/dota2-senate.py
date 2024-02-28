class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rem_d = 0
        rem_r = 0
        queue = deque(senate)
        while len(set(queue))>1:
            if queue[0] == "R":
                if rem_r == 0:
                    rem_d+=1
                    val = queue.popleft()
                    queue.append(val)
                while queue and rem_r>0 and queue[0]=="R":
                    rem_r -= 1
                    queue.popleft()
            else:
                if rem_d==0:
                    rem_r += 1
                    val = queue.popleft()
                    queue.append(val)
                while queue and rem_d>0 and queue[0] == "D":
                    rem_d -= 1
                    queue.popleft()
        if queue[0] == "R":
            return "Radiant"
        else:
            return "Dire"
