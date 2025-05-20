# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root,curSum):
            if not root:
                return False
            curSum+=root.val
            if not root.left and not root.right:
                return targetSum == curSum
            return has_sum(root.left, curSum) or has_sum(root.right, curSum)
        return has_sum(root, 0)
            