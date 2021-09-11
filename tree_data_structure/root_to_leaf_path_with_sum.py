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
    def solveA(self, A, B):
        res = []

        def solve(curr_set, curr_sum, node):
            if node is None:
                return
            if node.right is None and node.left is None:
                if curr_sum + node.val == B:
                    res.append(curr_set + [node.val])
                    return
                else:
                    return
            solve(curr_set + [node.val], curr_sum + node.val, node.left)
            solve(curr_set + [node.val], curr_sum + node.val, node.right)

        solve([], 0, A)
        return res

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
    B = 6
    print(bt.solveB())
