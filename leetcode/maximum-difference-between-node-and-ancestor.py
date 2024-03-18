# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def maxdiff(node,maxx,minn):
            nonlocal res
            if not node:
                return
            res = max(res,max(abs(maxx-node.val),abs(minn-node.val)))
            maxx = max(maxx,node.val)
            minn = min(minn,node.val)
            maxdiff(node.left,maxx,minn)
            maxdiff(node.right,maxx,minn)
        maxdiff(root,root.val,root.val)
        return res

