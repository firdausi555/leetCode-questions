# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None:
            return []
        ans=[]
        q=deque()
        q.append(root)
        while q:
            levelS=0
            count=len(q)
            for i in range(count):
                node =q.popleft()
                levelS+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(levelS/count)
        return ans 
