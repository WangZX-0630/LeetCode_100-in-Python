# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        self.dfs(root, depth)
        return self.max_depth

    def dfs(self, root, depth):
        if root is not None:
            depth += 1
            if self.max_depth < depth:
                self.max_depth = depth
            self.dfs(root.left, depth)
            self.dfs(root.right, depth)


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(val=1, left=TreeNode(val=2, left=None, right=TreeNode(val=1, left=None, right=None)),
                    right=TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=None))
    print(solution.maxDepth(tree))

