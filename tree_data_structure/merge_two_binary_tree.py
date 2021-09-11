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
    @staticmethod
    def helper(root1, root2):
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root = TreeNode(root1.val + root2.val)
        root.left = Solution.helper(root1.left, root2.left)
        root.right = Solution.helper(root1.right, root2.right)
        return root

    # interviewbit solution
    def solve(self, A, B):
        return Solution.helper(A, B)

    # merge binary tree recursive practice
    def solve2(self, root1, root2):
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.solve2(root1.left, root2.left)
        root.right = self.solve2(root1.right, root2.right)

        return root


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
    print(bt3.solve2(bt.root, bt2.root).val)    # prints the first node
