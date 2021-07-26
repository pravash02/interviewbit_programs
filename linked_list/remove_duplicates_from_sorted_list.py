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
        removeDup = ListNode(curr.val)
        head = removeDup
        while curr:
            if curr.val == removeDup.val:
                pass
            else:
                removeDup.next = ListNode(curr.val)
                removeDup = removeDup.next
            curr = curr.next
        return head

    def solveB(self):
        curr = self.head
        removeDup = Node(curr.val)
        head = removeDup
        while curr:
            if curr.val == removeDup.val:
                pass
            else:
                removeDup.next = Node(curr.val)
                removeDup = removeDup.next
            curr = curr.next
        return head

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

    print(mylist1.solveB())
