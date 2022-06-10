from math import log2, inf
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left = None if self.left is None else str(self.left)
        right = None if self.right is None else str(self.right)
        return f'[val: {self.val}, left: {left}, right: {right}]'


def create_tree_bfs_approach(nodes):
    head = None
    if not nodes:
        return head
    levels = int(log2(len(nodes) + 1))
    head = TreeNode(val=nodes[0])
    level_nodes = [(head, 0), ]
    for level in range(1, levels):
        next_level_base_ind = 2 ** level - 1
        next_level_nodes = []
        for cur_node, level_index in level_nodes:
            if cur_node:
                next_level_left_ind = next_level_base_ind + level_index * 2
                cur_node.left = None
                if nodes[next_level_left_ind] is not None:
                    cur_node.left = TreeNode(val=nodes[next_level_left_ind])
                next_level_nodes.append((cur_node.left, level_index * 2))

                next_level_right_ind = next_level_base_ind + level_index * 2 + 1
                cur_node.right = None
                if nodes[next_level_right_ind] is not None:
                    cur_node.right = TreeNode(val=nodes[next_level_right_ind])
                next_level_nodes.append((cur_node.right, level_index * 2 + 1))
        level_nodes = next_level_nodes
    return head


# TODO: Write DFS-oriented approach
def create_tree_dfs_approach(nodes):
    pass


class Solution:
    def is_valid_bst(self, root):
        return self.dfs(root, -inf, inf)

    def dfs(self, node, left_max, right_min):
        if not node:
            return True
        elif left_max < node.val < right_min:
            left = self.dfs(node.left, left_max, node.val)
            right = self.dfs(node.right, node.val, right_min)
            return left and right
        else:
            return False


if __name__ == '__main__':
    nodes = [5, 4, 6, None, None, 5.5, 7]
    head = create_tree_bfs_approach(nodes)
    print(head)
    s = Solution()
    print(s.is_valid_bst(head))


