# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root, k):
        if root==None:
            return None
        
        result = []
        q = deque()
        q.append(root)
        TotalL=0
        
        while q:
            size = len(q)
            level = []
            
            for i in range(size):
                node=TreeNode()
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            TotalL+=1
            
            result.append(sum(level))
        if k>TotalL:
            return -1
        
        return sorted(result)[-k]
        