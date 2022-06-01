# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        layer_num = 0
        layer_nodes = []
        for i in range(len(preorder)):



if __name__ == '__main__':
    solution = Solution()
