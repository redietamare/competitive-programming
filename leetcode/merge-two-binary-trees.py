# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1,node2):
            if node1 and node2:
                newroot = TreeNode(node1.val+node2.val)
                newroot.left = merge(node1.left,node2.left)
                newroot.right = merge(node1.right,node2.right)
                return newroot
            else:
                return node1 or node2
        return merge(root1,root2)
