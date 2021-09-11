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
    def solve(self, A):
        if A is not None:
            yield A.val
            yield from self.solve(A.left)
            yield from self.solve(A.right)

    # pre-order traversal iterative practice
    def solve2(self):
        arr = [self.root]
        preorder_traversal = []

        while len(arr) > 0:
            root = arr.pop()
            preorder_traversal.append(root.val)

            if root.right:
                arr.append(root.right)

            if root.left:
                arr.append(root.left)

        print(preorder_traversal)

    # pre-order traversal recurssive practice
    def solve3(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal += (str(start.val) + "->")
            traversal = self.solve3(start.left, traversal)
            traversal = self.solve3(start.right, traversal)
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

    bt.solve2()
    print(bt.solve3(bt.root, ''))

