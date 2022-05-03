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
    def solveA(self, root, target):
        if root is None:
            return target == 0

        else:
            res = 0
            target -= root.val

            if target == 0 and root.left is None and root.right is None:
                return 1

            if root.left:
                res = res or self.solveA(root.left, target)
            if root.right:
                res = res or self.solveA(root.right, target)

            return res

    # path sum - binary tree recursive practice
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
    B = 6
    print(bt.solveA(bt.root, B))
