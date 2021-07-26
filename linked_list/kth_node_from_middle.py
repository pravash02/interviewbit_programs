class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A, B):
        n = self.getCount(A)
        reqNode = int((n / 2 + 1) - B)

        if reqNode <= 0:
            return -1
        else:
            current = A
            count = 1
            while current:
                if count == reqNode:
                    return current.val
                count += 1
                current = current.next
        return A

    def getCount(self, h):
        count = 0
        current = h
        while current:
            count += 1
            current = current.next

        return count

    ### practice with custom inputs
    def solveB(self, B):
        n = self.count()
        mid_node = (n//2) + 1
        req_node = mid_node - B     # this will give the number of elements to travers
        if req_node <= 0:
            return -1
        else:
            cur = self.head
            count = 1
            while cur:
                if count == req_node:
                    return cur.val
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

    B = 3
    print(mylist.solveB(B))
