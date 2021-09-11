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
        self.node = []

    # interviewbit solution
    def solveA(self, A):
        def node_collect(A):
            self.node.append(A)
            if A.left:
                node_collect(A.left)
            if A.right:
                node_collect(A.right)
            return

        node_collect(A)
        for i in range(1, len(self.node)):
            self.node[i - 1].right = self.node[i]
            self.node[i - 1].left = None
        return A

    # flatten binary tree to linked list recursive practice
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
