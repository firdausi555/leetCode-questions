# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def helper(node, current_path, current_sum):
            if not node:
                return

            current_path.append(node.val)
            current_sum += node.val

            if not node.left and not node.right:
                if current_sum == targetSum:
                    ans.append(list(current_path))  # Make a copy of the current path

           
            helper(node.left, current_path, current_sum)
            helper(node.right, current_path, current_sum)

            current_path.pop()

        helper(root, [], 0)
        return ans
