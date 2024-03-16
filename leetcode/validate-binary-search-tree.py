# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ans = []
        # def validity(node):
        #     if node:
        #         validity(node.left)
        #         ans.append(node.val)
        #         validity(node.right)
        # validity(root)
        # print(ans)
        # for i in range(1,len(ans)):
        #     if ans[i]<=ans[i-1]:
        #         return False
        # return True
        def validity(l_bound,r_bound,node):
            if not node:
                return True
            if l_bound>=node.val or node.val>=r_bound:
                return False
            left = validity(l_bound,node.val,node.left)
            right = validity(node.val,r_bound,node.right)
            return left and right

        return validity(float("-inf"),float("inf"),root)