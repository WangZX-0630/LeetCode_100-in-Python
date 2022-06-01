# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        layer_nodes = [root]
        while len(layer_nodes) > 0:
            n = len(layer_nodes)
            for i in range(n):
                layer_nodes.append(layer_nodes[0].left)
                layer_nodes.append(layer_nodes[0].right)
                layer_nodes.pop(0)
            for j in range(n):
                if layer_nodes[j] is None and layer_nodes[2 * n - 1 - j] is None:
                    continue
                elif layer_nodes[j] is None or layer_nodes[2 * n - 1 - j] is None:
                    return False
                elif layer_nodes[j].val != layer_nodes[2 * n - 1 - j].val:
                    return False

            layer_nodes = list(filter(None, layer_nodes))
        return True


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(val=1, left=TreeNode(val=2, left=None, right=TreeNode(val=1, left=None, right=None)),
                    right=TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=None))
    print(solution.isSymmetric(tree))
