class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A, B):
        n = 0
        curr = A
        while curr:
            n += 1
            curr = curr.next
        if n <= B:
            return A.next
        toDrop = n - B
        i = 1
        curr = A
        head = curr
        while curr:
            if i != toDrop:
                i += 1
            else:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head

    ### practice with custom inputs
    def solveB(self, B):
        n = self.count()
        req_node = n - B     # this will give the number of elements to traverse

        cur = self.head
        count = 1
        while cur:
            if count == req_node:
                cur.next = cur.next.next
                break
            count += 1
            cur = cur.next
        return self.head

    def count(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

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
    mylist = ListNode()
    lst = [3, 4, 7, 5, 6, 16, 15, 61, 16]
    for i in range(0, len(lst)):
        mylist.push_at_begining(lst[i])

    B = 2
    print(mylist.solveB(B))
