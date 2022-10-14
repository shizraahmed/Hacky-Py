# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, 0)]

        while stack:
            node, mem = stack.pop()
            if node:
                res = mem + node.val
                if not any([node.left, node.right]) and res == targetSum:
                    return True

                stack.append((node.left, res))
                stack.append((node.right, res))

        return False


# Time O(n)
# Space O(n)
