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
        if len(A) == 0 and len(B) == 0:
            return None
        root = B[-1]
        index = A.index(root)
        new_node = TreeNode(root)

        new_node.left = self.solveA(A[:index], B[:index])
        new_node.right = self.solveA(A[index + 1:], B[index:-1])
        return new_node

    # interview solution
    def solveB(self, A, B):
        pass

    # practice
    def solveC(self, A, B):
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
    A = [2, 1, 3]
    B = [2, 3, 1]
    print(bt.solveC(A, B))
