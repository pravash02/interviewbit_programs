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

    # interview solution
    def solveA(self, A):
        if (not A):
            return None
        else:
            if A.left and not A.right:
                return self.solveA(A.left)
            elif A.right and not A.left:
                return self.solveA(A.right)
            A.left = self.solveA(A.left)
            A.right = self.solveA(A.right)
            return A

    # path to given node recursive practice
    def solveC(self):
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

    print(bt.solveC())
