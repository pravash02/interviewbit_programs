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

    def __init__(self, A):
        BinaryTree.__init__(self, A)

    # interviewbit solution
    def solveA(self, A):
        return 0 if self.findheight(A, 0) == -1 else 1

    # interviewbit solution
    def findheight(self, A, depth):
        if not A.left and not A.right:
            return depth

        left_height = 0
        right_height = 0

        if A.left:
            left_height = self.findheight(A.left, depth + 1)

        if A.right:
            right_height = self.findheight(A.right, depth + 1)

        if left_height == -1 or right_height == -1:
            return -1

        if left_height - right_height > 1:
            return -1
        else:
            return max(left_height, right_height)

    # balanced binary tree recursive practice
    def solveB(self):
        pass


if __name__ == '__main__':
    # bt = BinaryTree(1)
    bt = Solution(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)
    bt.root.right.left = TreeNode(6)
    bt.root.right.right = TreeNode(7)

    print(bt.solveB())
