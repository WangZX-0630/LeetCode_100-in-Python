# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []
        self.printTree(root, return_list)
        return return_list

    def printTree(self, root, return_list):
        if root is not None:
            self.printTree(root.left, return_list)
            return_list.append(root.val)
            self.printTree(root.right, return_list)


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
    print(solution.inorderTraversal(tree))



