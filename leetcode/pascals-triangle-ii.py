class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #recursion
       
        def pascal(triangle,rowIndex,r,ans):
            if r == rowIndex:
                return triangle
            ans.append(1)
            for i in range(1,len(triangle)):
                ans.append(triangle[i-1]+triangle[i])
            ans.append(1)
            r+=1
            triangle= ans.copy()
            arr = []
            return pascal(triangle,rowIndex,r,[])
        return (pascal([1],rowIndex,0,[]))








        #iterative way
        # triangle = [1]
        # ans = []
        
        
        # for j in range(rowIndex):
        #     ans.append(1)
        #     for i in range(1,len(triangle)):
        #         ans.append(triangle[i-1]+triangle[i])
        #     ans.append(1)
        #     triangle = ans.copy()
        #     ans = []
        # return triangle