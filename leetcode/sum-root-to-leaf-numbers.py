# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def sumtorootleaf(node,curr):
            if not node:
                return
            if node and not node.right and not node.left:
                curr += str(node.val)
                ans.append(curr)
                return
            curr+= str(node.val)
            sumtorootleaf(node.left,curr)
            sumtorootleaf(node.right,curr)
        sumtorootleaf(root,"")
        for i , num in enumerate(ans):
            ans[i] = int(num)
        return sum(ans)