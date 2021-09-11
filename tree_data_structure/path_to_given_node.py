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
        self.path = list()

    # interviewbit solution
    def solveA(self, A, B):
        if self.helper(A, B):
            return self.path

    # interviewbit solution
    def helper(self, A, B):
        if not A:
            return False

        self.path.append(A.val)
        if A.val == B:
            return True

        if self.helper(A.left, B) or self.helper(A.right, B):
            return True

        self.path.pop(-1)
        return False

    # practice
    def solveB(self, B):
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
    B = 5
    print(bt.solveB(B))
