# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        else:
            layer_nodes = [root]
            result_list = [[root.val]]
            layer_num = 1
            while len(layer_nodes) != 0:
                n = len(layer_nodes)
                for i in range(n):
                    layer_nodes.append(layer_nodes[0].left)
                    layer_nodes.append(layer_nodes[0].right)
                    layer_nodes.pop(0)
                layer_nodes = list(filter(None, layer_nodes))
                if len(layer_nodes) == 0:
                    break
                result_list.append([])
                for j in range(len(layer_nodes)):
                    result_list[layer_num].append(layer_nodes[j].val)
                layer_num += 1
            return result_list


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(val=1, left=TreeNode(val=2, left=None, right=TreeNode(val=1, left=None, right=None)),
                    right=TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=None))
    print(solution.levelOrder(tree))
