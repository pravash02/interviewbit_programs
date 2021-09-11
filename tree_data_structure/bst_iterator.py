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
        self.stack = []
        self.current = A
        self.has_next = bool(A)

    # interviewbit solution
    def hasNext(self):
        return self.has_next

    # interviewbit solution
    def solveA(self, root, target):
        next_val = None
        if self.has_next:
            while self.current is not None:
                self.stack.append(self.current)
                self.current = self.current.left
            if self.stack:
                self.current = self.stack.pop()
                next_val = self.current.val
                self.current = self.current.right
            if not self.current and not self.stack:
                self.has_next = False

        return next_val

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
    print(bt.solveB())
