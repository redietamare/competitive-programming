# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        parent = root
        if not parent:
            return ans
        ans.append(parent.val)
        left = self.preorderTraversal(parent.left)
        ans.extend(left)
        right = self.preorderTraversal(parent.right)
        ans.extend(right)
        return ans
        

