class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashmap=defaultdict(list)
        ans = []
     
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                hashmap[i+j].append(mat[i][j])
              
        print(hashmap)
        for i in hashmap:
           
            if i%2==0:
                ans.extend(hashmap[i][::-1])        
            else:
                ans.extend(hashmap[i])
        return ans
        
        
        
        
        
        
  
        
        
#         m=len(mat)
#         n=len(mat[0])
#         diagonals= m+n-1
#         ans = []
#         for d in range(diagonals):

#             if d%2==0:
#                 i=min(d,m-1)
#                 j=max(0,(d-(m-1)))
#                 while i>=0 and j<n:
#                     ans.append(mat[i][j])
#                     i-=1
#                     j+=1
#             else:
#                 i=max(0,d-(n-1))
#                 j=min(d,n-1)
#                 while i<m and j>=0:
#                     ans.append(mat[i][j])
#                     i+=1
#                     j-=1
#         return(ans)