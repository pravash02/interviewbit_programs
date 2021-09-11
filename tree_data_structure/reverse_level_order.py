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
        if A is None:
            return None
        q = []
        res = []
        q.append(A)
        while len(q) != 0:
            node = q.pop(0)
            res.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            res = res[::-1]

        return res

    # interviewbit solution
    def solveB(self, A):
        pass

    # reverse level order binary tree recursive practice
    def solveC(self):
        A = self.root
        if A is None:
            return None
        q = []
        res = []
        q.append(A)
        while len(q) != 0:
            node = q.pop(0)
            res.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            res = res[::-1]

        return res


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
