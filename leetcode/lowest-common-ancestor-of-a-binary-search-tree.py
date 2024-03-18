# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowest(node):
            if not node:
                return 
            if node.val == p.val or node.val == q.val:
                return node
            elif node.val > min(q.val,p.val) and node.val < max(q.val,p.val):
                return node
            elif node.val > max(q.val,p.val):
                return lowest(node.left)
            elif node.val < min(q.val,p.val):
                return lowest(node.right)
        return lowest(root)
            