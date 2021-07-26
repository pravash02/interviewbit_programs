class Node:
    # Function to initialize the node object
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode:
    # Function to initialize the Linked List
    def __init__(self):
        self.head = None

    ### interviewbit solution
    def solve(self, A, B):
        if A is None:
            return A

        aa = []
        while A:
            aa.append(A.val)
            A = A.next

        i = 0
        bb = bc = []
        while i < len(aa):
            if aa[i] < B:
                bb.append(aa[i])
            else:
                bc.append(aa[i])
            i += 1

        cc = []
        for each in bb:
            cc.append(each)
        for each in bc:
            cc.append(each)

        head = Node(cc[0])
        cur = head
        for i in range(1, len(cc)):
            cur.next = Node(cc[i])  # pushing element of list in linked list through loop
            cur = cur.next
        return head

    ### practice with custom inputs
    def solveB(self, B):
        if self.head is None:
            return self.head

        aa = []
        cur = self.head
        while cur:
            aa.append(cur.val)
            cur = cur.next

        i = 0
        bb = []
        bc = []
        while i < len(aa):
            if aa[i] < B:
                bb.append(aa[i])
            else:
                bc.append(aa[i])
            i += 1

        cc = []
        for each in bb:
            cc.append(each)
        for each in bc:
            cc.append(each)

        head = Node(cc[0])
        cur = head
        for i in range(1, len(cc)):
            cur.next = Node(cc[i])  # pushing element of list in linked list through loop
            cur = cur.next
        return head

    def push_at_begining(self, lst):
        self.head = Node(lst[0])
        cur = self.head
        for i in range(1, len(lst)):
            cur.next = Node(lst[i])
            cur = cur.next

    def printList(self):
        lst = []
        temp = self.head
        while temp is not None:
            lst.append(temp.val)
            temp = temp.next
        print(lst)


if __name__ == '__main__':
    mylist = ListNode()
    lst = [1, 3, 4, 2, 5, 2]
    B = 3
    mylist.push_at_begining(lst)

    mylist.printList()
    print(mylist.solveB(B))
