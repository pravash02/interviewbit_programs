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
        stack = []
        res = []
        curr = A
        while stack or curr:
            while curr:
                res.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                curr = curr.right
            if stack:
                curr = stack.pop()
        return res[::-1]

    # post-order traversal iterative practice
    def solve2(self):
        arr = [self.root]
        preorder_traversal = []

        while len(arr) > 0:
            root = arr.pop()
            preorder_traversal.append(root.val)

            if root.left:
                arr.append(root.left)

            if root.right:
                arr.append(root.right)

        print(preorder_traversal[::-1])

    # post-order traversal recurssive practice
    def solve3(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.solve3(start.left, traversal)
            traversal = self.solve3(start.right, traversal)
            traversal += (str(start.val) + "->")
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

