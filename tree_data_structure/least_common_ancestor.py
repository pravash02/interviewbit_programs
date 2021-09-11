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
    def solveA(self, A, B, C):
        if not self.contains(A, B) or not self.contains(A, C):
            return -1
        lca = self.findLCA(A, B, C)
        if lca:
            return lca
        return -1

    # interviewbit solution
    def contains(self, root, val):
        if root is None:
            return False
        if root.val == val:
            return True

        return self.contains(root.left, val) or self.contains(root.right, val)

    # interviewbit solution
    def findLCA(self, A, B, C):
        if A is None:
            return None
        if A.val == B or A.val == C:
            return A.val
        left_ = self.findLCA(A.left, B, C)
        right_ = self.findLCA(A.right, B, C)
        if left_ and right_:
            return A.val
        if left_:
            return left_
        if right_:
            return right_
        return None

    # least common ancestor - binary tree recursive practice
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
    B = 2
    C = 3
    print(bt.solveB())
