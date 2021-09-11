# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    # def solve2(self):
    #     in_order = []
    #     stack = []
    #     t = self.root
    #     while True:
    #         if t is not None:
    #             stack.append(t)
    #             t = t.left
    #         elif stack:
    #             t = stack.pop()
    #             in_order.append(t.val)
    #             t = t.right
    #         else:
    #             break
    #     print(in_order)


class Solution(BinaryTree):

    def __init__(self, A):
        BinaryTree.__init__(self, A)

    # interviewbit solution
    def solve(self, A):
        t = A
        stack = []
        inorder = []
        while stack != [] or t is not None:
            if t is not None:
                stack.append(t)
                t = t.left
            else:
                t = stack.pop()
                inorder.append(t.val)
                t = t.right
        return inorder

    # in-order traversal iterative practice
    def solve2(self):
        in_order = []
        stack = []
        t = self.root
        while True:
            if t is not None:
                stack.append(t)
                t = t.left
            elif stack:
                t = stack.pop()
                in_order.append(t.val)
                t = t.right
            else:
                break
        print(in_order)

    # in-order traversal recurssive practice
    def solve3(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.solve3(start.left, traversal)
            traversal += (str(start.val) + "->")
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

