# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def mode(node):
            if node:
                print(node.val)
                ans.append(node.val)
                mode(node.left)
                mode(node.right)
        mode(root)
        res = []
        count = Counter(ans)
        maxx =  max(count.values())
        print(count)
        for i in count:
            if count[i] == maxx:
                res.append(i)
        return res