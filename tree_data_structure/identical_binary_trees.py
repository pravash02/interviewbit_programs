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
    def isSameTree(self, root_A, root_B):
        if root_A is None and root_B is None:
            pass
        elif root_A is None or root_B is None:
            return 0
        elif not self.isSameNode(root_A, root_B):
            return 0
        else:
            if self.isSameTree(root_A.left, root_B.left) == 0 or \
                    self.isSameTree(root_A.right, root_B.right) == 0:
                return 0
        return 1

    # interviewbit solution
    def isSameNode(self, node_A, node_B):
        if node_A.val != node_B.val:
            return 0
        return 1

    # check identical practice iterative
    def solve2(self, root_A, root_B):
        if root_A is None and root_B is None:
            pass
        elif root_A is None or root_B is None:
            return 0
        elif not self.isSameNode_(root_A, root_B):
            return 0
        else:
            if self.solve2(root_A.left, root_B.left) == 0 or \
                    self.solve2(root_A.right, root_B.right) == 0:
                return 0
        return 1

    # check identical practice iterative
    def isSameNode_(self, node_A, node_B):
        if node_A.val != node_B.val:
            return 0
        return 1

    # check identical practice recursive
    def solve3(self, A, B):
        if self.inorder_t(A, '') == self.inorder_t(B, ''):
            return 1
        return 0

    def inorder_t(self, root, traversal):
        if root:
            traversal = self.inorder_t(root.left, traversal)
            traversal += str(root.val)
            traversal = self.inorder_t(root.right, traversal)
        return traversal


if __name__ == '__main__':
    # bt = BinaryTree(1)
    bt = Solution(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)
    bt.root.right.left = TreeNode(6)
    bt.root.right.right = TreeNode(7)

    bt2 = Solution(1)
    bt2.root.left = TreeNode(2)
    bt2.root.right = TreeNode(3)
    bt2.root.left.left = TreeNode(4)
    bt2.root.left.right = TreeNode(5)
    bt2.root.right.left = TreeNode(6)
    bt2.root.right.right = TreeNode(7)

    bt3 = Solution(0)
    print(bt3.solve2(bt.root, bt2.root))
