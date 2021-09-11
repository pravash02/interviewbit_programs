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
        def helper(root1, root2):
            if not root1 and not root2:
                return 1
            if not root1 or not root2:
                return 0
            return int(root1.val == root2.val and helper(root1.left, root2.right) \
                       and helper(root2.left, root1.right))
        if not A:
            return 1
        return helper(A.left, A.right)


    # interviewbit solution
    def solveB(self, A):
        TL = A.left
        TR = A.right
        def check_symm(TL, TR):
            TL_val = TL.val if TL else -1
            TR_val = TR.val if TR else -1
            if not TL and not TR:
                return 1
            if TL_val != TR_val:
                return 0
            else:
                L_check = check_symm(TL.left, TR.right)
                R_check = check_symm(TL.right, TR.left)
                return min(L_check, R_check)

        return check_symm(A.left, A.right)

    # symmetric binary tree recursive practice
    def solveC(self):
        root = self.root

        def check_symmetric(root_left, root_right):
            if not root_left and not root_right:
                return 1
            elif not root_left or not root_right:
                return 0
            else:
                return int(root_left.val == root_right.val) and \
                       check_symmetric(root_left.left, root_right.left) and \
                       check_symmetric(root_left.right, root_right.right)

        return check_symmetric(root.left, root.right)


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
