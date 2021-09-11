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
        queue = []
        queue.append([A, 0])
        res = []
        prev = -1
        queue_index = 0
        while queue_index < len(queue):
            root, level = queue[queue_index]
            if root.right:
                queue.append([root.right, level + 1])
            if root.left:
                queue.append([root.left, level + 1])
            if prev != level:
                res.append(root.val)
            queue_index += 1
            prev = level

        return res

    # interviewbit solution
    def solveB(self, A):
        def hlp(A, mem, dep):
            if A is None:
                return
            hlp(A.left, mem, dep + 1)
            mem[dep] = A.val
            hlp(A.right, mem, dep + 1)

        mem = {}
        hlp(A, mem, 0)
        ans = [mem[key] for key in sorted(mem)]
        return ans

    # right view of binary tree recursive practice
    def solveC(self):
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
