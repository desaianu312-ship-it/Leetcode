# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        max_count = 0
        count = 0
        prev = None

        def inorder(node):
            nonlocal count, max_count, prev

            if not node:
                return

            inorder(node.left)

            if node.val == prev:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                result.clear()
                result.append(node.val)
            elif count == max_count:
                result.append(node.val)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return result
        