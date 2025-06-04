# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root== None:
            return None
        temp=root.val

        if temp < p.val and temp < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif temp > p.val and temp > q.val:
            return self.lowestCommonAncestor(root.left, p,q)
        return root
