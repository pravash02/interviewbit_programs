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
        if (len(A) == 0):
            return None
        n = len(A) / 2
        K = TreeNode(A[n])
        K.left = self.solveA(A[:n])
        K.right = self.solveA(A[n + 1:])
        return K

    # interviewbit solution
    def solveB(self, A):
        pass

    # inorder traversal of cartesian tree recursive practice
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
