class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A):
        curr = A
        head = prev = Node(None)
        head.next = curr

        while curr and curr.next:

            if curr.val == curr.next.val:
                while (curr and curr.next and
                       curr.val == curr.next.val):
                    curr = curr.next

                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return head.next

    ### interviewbit solution using recurssion
    import sys
    sys.setrecursionlimit(10000)
    def solveB(self, root):
        if not root or not root.next:
            return root

        if root.next.val != root.val:
            root.next = self.solveB(root.next)
            return root

        while root.next and root.next.val == root.val:
            root = root.next

        root = self.solveB(root.next)
        return root

    ### practice with custom inputs
    def solveC(self):
        cur = self.head
        res = set()

        while cur is not None and cur.next is not None:
            if cur.val not in res:
                res.add(cur.val)
            cur = cur.next

        res = list(res)
        temp = Node(res[0])
        cur = temp
        for i in range(1, len(res)):
            cur.next = Node(res[i])
            cur = cur.next

        return temp

    def push_at_begining(self, node_data):
        new_node = Node(node_data)
        new_node.next = None
        cur = self.head
        if cur is None:
            self.head = new_node
            return
        else:
            while cur.next is not None:
                cur = cur.next
        cur.next = new_node


if __name__ == '__main__':
    mylist1 = ListNode()
    lst1 = [1, 2, 2, 3, 3]

    for i in range(0, len(lst1)):
        mylist1.push_at_begining(lst1[i])

    print(mylist1.solveC())

