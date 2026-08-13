# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        ans = float("inf")

        def inorder(node):
            nonlocal prev, ans

            if not node:
                return

            inorder(node.left)

            if prev is not None:
                ans = min(ans, node.val - prev)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return ans
        