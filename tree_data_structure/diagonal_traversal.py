from collections import deque


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)


class Solution(BinaryTree):
    # interviewbit solution
    def diagonal(self, array1, array, left):
        for node in array1:
            while True:
                array.append(node.val)
                if node.left:
                    left.append(node.left)
                if node.right:
                    node = node.right
                else:
                    break

    # interviewbit solution
    def solve(self, A):
        final_array, left1 = [], [A]
        while True:
            array, left2 = [], []
            self.diagonal(left1, array, left2)
            final_array += array
            if len(left2) == 0:
                break
            left1 = left2
        return final_array

    # diagonal traversal iterative practice
    def __init__(self, value):
        BinaryTree.__init__(self, value)

    def solve2(self):
        root = self.root
        arr = deque()
        diagonal_order = []

        while root:
            diagonal_order.append(root.val)

            if root.left:
                arr.appendleft(root.left)

            if root.right:
                root = root.right
            else:
                if len(arr) >= 1:
                    root = arr.pop()
                else:
                    root = None

        return diagonal_order


if __name__ == '__main__':
    # bt = BinaryTree(1)
    bt = Solution(8)
    bt.root.left = TreeNode(3)
    bt.root.right = TreeNode(10)
    bt.root.left.left = TreeNode(1)
    bt.root.left.right = TreeNode(6)
    bt.root.right.right = TreeNode(14)
    bt.root.right.right.left = TreeNode(13)
    bt.root.left.right.left = TreeNode(4)
    bt.root.left.right.right = TreeNode(7)

    print(bt.solve2())

