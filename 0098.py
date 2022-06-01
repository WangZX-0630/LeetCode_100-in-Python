# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorderList = []
        self.printTree(root, inorderList)
        for i in range(len(inorderList) - 1):
            if inorderList[i] >= inorderList[i + 1]:
                return False
        return True

    def printTree(self, root, inorderList):
        if root is not None:
            self.printTree(root.left, inorderList)
            inorderList.append(root.val)
            self.printTree(root.right, inorderList)


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=1.5, left=None, right=None), right=None))
    print(solution.isValidBST(tree))

