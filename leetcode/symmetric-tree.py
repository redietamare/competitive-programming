# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left,right):
            if left and right:
                if left.val != right.val:
                    return False
                return symmetric(left.left,right.right) and symmetric(left.right,right.left)
            if not left and not right:
                return True
            else:
                return False
        return(symmetric(root.left,root.right))
            