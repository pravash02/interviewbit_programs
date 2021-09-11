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
        if A:
            root = TreeNode(A[0])
            idx = B.index(A[0])
            root.left = self.solveA(A[1:idx + 1], B[:idx + 1])
            root.right = self.solveA(A[idx + 1:], B[idx + 1:])
            return root

    # interview solution
    def solveB(self, A, B):
        preorderArr = A
        inorderArr = B
        if not preorderArr:
            return None
        root = TreeNode(preorderArr[0])
        rootIdx = self.findRoot(root, inorderArr)
        # divide the remaining into left and right subtrees
        leftInorder = inorderArr[:rootIdx]
        rightInorder = inorderArr[rootIdx + 1:]
        # the lengths of subtrees in each array would be the same
        leftn = len(leftInorder)
        rightn = len(rightInorder)
        leftPreorder = preorderArr[1:1 + leftn]
        rightPreorder = preorderArr[1 + leftn:1 + leftn + rightn]

        root.left = self.solveB(leftPreorder, leftInorder)
        root.right = self.solveB(rightPreorder, rightInorder)
        return root

    # interview solution
    def findRoot(self, root, inorderArr):
        for i in range(len(inorderArr)):
            if root.val == inorderArr[i]:
                return i

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
    B = [1, 2, 3]
    print(bt.solveC(A, B))
