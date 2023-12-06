class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_dis = abs(0 - target[0]) + abs(0 - target[1])
        print(my_dis)
        for ghost in ghosts:
            if ghost[0]*target[0] >= 0:
                d1=abs(ghost[0]-target[0])
            else:
                d1=abs(ghost[0]) + abs(target[0])
            
            if ghost[1]*target[1] >= 0:
                d2=abs(ghost[1]-target[1])
            else:
                d2=abs(ghost[1]) + abs(target[1])
                
            ghost_dis = d1 + d2
    
            if ghost_dis <= my_dis :
                return False
            
        return True