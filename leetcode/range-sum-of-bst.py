# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangesum(node):
            if not node:
                return 0
            curr = 0
            if node.val>= low and node.val <=high:
                curr+=node.val
            curr += rangesum(node.left)
            curr += rangesum(node.right)
            return curr
        
            
        return rangesum(root)